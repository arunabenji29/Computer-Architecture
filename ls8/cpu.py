# """CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.sp = 0b11110100

    def ram_read(self,address):
        MAR = address
        return self.ram[address]

    def ram_write(self,address,value):
        MDR = value
        self.ram[address] = value

    def load(self,filename):
        """Load a program into memory."""

        try:

            address = 0

            with open(filename) as f:
                for line in f:
                    # print(f'\n\n{line}')
                    hash_split = line.split("#")
                    # print(f'hash split: {hash_split}')    
                    binary_code = hash_split[0].strip()
                    # print(f'binary code {type(binary_code)}')
                    try:
                        if binary_code is not None:
                            # val = int(f'0b{binary_code}',2)
                            val = int(binary_code)
                    except ValueError:
                        continue
                    # print(f'val: {val}')
                    self.ram_write(address,val)
                    address += 1

        except FileNotFoundError:
            print(f"{sys.argv[0]} : {sys.argv[1]} not found")
            sys.exit(1)
        # print(f'Ram contents: {self.ram}')

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        IR  = self.pc
        operand_a = self.ram_read(self.pc+1)
        operand_b = self.ram_read(self.pc+2)

        running = True
        curr_addr = 0

        while running:
            # self.trace()
            if int(f'{self.ram_read(curr_addr)}',2) == 130 :
                self.reg[int(f'{self.ram_read(curr_addr+1)}',2)] = int(f'{self.ram_read(curr_addr+2)}',2)
                # print(f"load: register{int(f'{self.ram_read(curr_addr+1)}',2)} value:{self.reg[int(f'{self.ram_read(curr_addr+1)}',2)]}")
                shift = int(f'{self.ram_read(curr_addr)}',2)
                incr = shift >> 6
                curr_addr += (incr + 1)

            elif int(f'{self.ram_read(curr_addr)}',2) == 71:
                bina = self.reg[int(f'{self.ram_read(curr_addr+1)}',2)]
                # print(f"print value at register:R{int(f'{self.ram_read(curr_addr+1)}',2)},value: {int(f'{bina}',2)}")
                shift = int(f'{self.ram_read(curr_addr)}',2)
                incr = shift >> 6
                curr_addr += (incr + 1)

            elif int(f'{self.ram_read(curr_addr)}',2) == 162:
                self.alu('MUL',self.ram_read(curr_addr+1),self.ram_read(curr_addr+2))
                print(f"mul result: {self.reg[0]} conv to int: {int(f'{self.reg[0]}',2)}")
                shift = int(f'{self.ram_read(curr_addr)}',2)
                incr = shift >> 6
                curr_addr += (incr + 1)

            elif int(f'{self.ram_read(curr_addr)}',2) == 160:
                self.alu('ADD',self.ram_read(curr_addr+1),self.ram_read(curr_addr+2))
                print(f"add result: {self.reg[0]}")
                shift = int(f'{self.ram_read(curr_addr)}',2)
                incr = shift >> 6
                curr_addr += (incr + 1)

            elif int(f'{self.ram_read(curr_addr)}',2) == 69:
                self.reg[7] = self.reg[self.ram_read(curr_addr+1)]
                self.sp -= 1
                self.ram_write(self.sp,self.reg[7])
                
                shift = int(f'{self.ram_read(curr_addr)}',2)
                incr = shift >> 6
                curr_addr += (incr + 1)

            elif int(f'{self.ram_read(curr_addr)}',2) == 70:

                self.reg[int(f'{self.ram_read(curr_addr+1)}',2)] = self.ram[self.sp]
                self.sp += 1
                shift = int(f'{self.ram_read(curr_addr)}',2)
                incr = shift >> 6
                curr_addr += (incr + 1)

            elif int(f'{self.ram_read(curr_addr)}',2) == 1:
                sys.exit(1)

            elif int(f'{self.ram_read(curr_addr)}',2) == 80:
                # Push the return address on the stack. 
                # This allows us to return to where we left off when the subroutine finishes executing.
                # The PC is set to the address stored in the given register. 
                # We jump to that location in RAM and execute the first instruction in the subroutine. 
                # The PC can move forward or backwards from its current location.
                self.sp -= 1
                # print(f'call: {self.sp}')
                # print(f"pc value: {curr_addr+2}")
                self.ram_write(self.sp,curr_addr+2)
                # print(f"address: {self.reg[self.ram_read(curr_addr+1)]}")

                curr_addr = self.reg[self.ram_read(curr_addr+1)]

        
            elif int(f'{self.ram_read(curr_addr)}',2) == 17:
                # Pop the value from the top of the stack and store it in the PC.
                curr_addr = self.ram_read(self.sp)
                self.sp += 1
                print(f'returned value: {curr_addr}')
