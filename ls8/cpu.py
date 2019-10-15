"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0

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

            if int(f'{self.ram_read(curr_addr)}',2) == 130 :
                self.reg[self.ram_read(curr_addr+1)] = self.ram_read(curr_addr+2)
                # print(f'Register value {self.reg[self.ram_read(curr_addr+1)]}')
                shift = int(f'{self.ram_read(curr_addr)}',2)
                incr = shift >> 6
                curr_addr += (incr + 1)

            elif int(f'{self.ram_read(curr_addr)}',2) == 71:
                print(self.reg[self.ram_read(curr_addr+1)])
                shift = int(f'{self.ram_read(curr_addr)}',2)
                incr = shift >> 6
                curr_addr += (incr + 1)

            elif int(f'{self.ram_read(curr_addr)}',2) == 162:
                self.alu('MUL',self.ram_read(curr_addr+1),self.ram_read(curr_addr+2))
                print(f"mul result: {self.reg[0]} conv to int: {int(f'{self.reg[0]}',2)}")
                shift = int(f'{self.ram_read(curr_addr)}',2)
                incr = shift >> 6
                curr_addr += (incr + 1)

            elif int(f'{self.ram_read(curr_addr)}',2) == 1:
                sys.exit(1)

        

# cpu = CPU()

# cpu.run()