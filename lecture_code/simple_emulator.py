import sys

PRINT_BEEJ      = 1
HALT            = 2
PRINT_NUM       = 3
SAVE            = 4
PRINT_REGISTER  = 5
ADD             = 6

memory = [
    PRINT_BEEJ,
    SAVE,
    65,
    2,
    SAVE,
    20,
    3,
    ADD,
    2,
    3,
    PRINT_REGISTER,
    2,
    HALT,
]

# memory = [
#     PRINT_BEEJ,
#     PRINT_NUM,
#     1,
#     PRINT_NUM,
#     12,
#     PRINT_BEEJ,
#     PRINT_NUM,
#     27,
#     PRINT_BEEJ,
#     PRINT_BEEJ,
#     PRINT_BEEJ,
#     HALT
# ]

pc = 0
running = True

# Create 8 registers
register = [0] * 8

while running:
    #do stuff
    command = memory[pc]
    print(f'memory[{pc}] : {memory[pc]}')
    print(f'command : {command}')

    if command == PRINT_BEEJ:
        print("BEEJ!")
        pc += 1

    elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 2

    elif command == HALT:
        running = False
        pc += 1

    elif command == SAVE:
        num = memory[pc+1] #Get the num from 1st arg
        reg = memory[pc+2]  #Get the register index from 2nd arg
        register[reg] = num #Store the num in the right register
        pc += 3

    elif command == PRINT_REGISTER:
        reg = memory[pc+1]  #Get the register index from 1st arg
        print(register[reg])    #Print the contents of that register
        pc += 2

    elif command == ADD:
        reg_a = memory[pc+1]    #Get the 1st register index from 1st arg
        reg_b = memory[pc+2]    #Get the 2nd register index from 2nd arg
        register[reg_a] += register[reg_b] #add registers, store in reg_a
        pc += 3

    else:
        print("Unknown Instruction: {command}")
        sys.exit(1)


# str = "101110"
# ​
# def to_decimal(num_string, base):
#     digit_list = list(num_string)
#     digit_list.reverse()
#     value = 0
#     for i in range(len(digit_list)):
#         print(f"+({int(digit_list[i])} * {base ** i})")
#         value += int(digit_list[i]) * (base ** i)
#     return value
# ​
# to_decimal(str, 2)


#second day
# import sys
# ​
# PRINT_BEEJ     = 1
# HALT           = 2
# PRINT_NUM      = 3
# SAVE           = 4  # SAVE VALUE INTO REGISTER
# PRINT_REGISTER = 5
# ADD            = 6
# ​
# ​
# # 256 bytes of memory
# memory = [0] * 16
# ​
# # Create 8 registers, 1 byte each
# register = [0] * 8
# ​
# ​
# pc = 0
# running = True
# ​
# ​
# def load_memory(filename):
#     try:
#         address = 0
# ​
#         with open(filename) as f:
#             for line in f:
#                 # Process comments:
#                 # Ignore anything after a # symbol
#                 comment_split = line.split("#")
# ​
#                 # Convert any numbers from binary strings to integers
#                 num = comment_split[0].strip()
#                 try:
#                     val = int(num)
#                 except ValueError:
#                     continue
# ​
#                 memory[address] = val
#                 address += 1
#                 # print(f"{val:08b}: {val:d}")
# ​
#     except FileNotFoundError:
#         print(f"{sys.argv[0]}: {sys.argv[1]} not found")
#         sys.exit(2)
# ​
# ​
# ​
# if len(sys.argv) != 2:
#     print("usage: simple.py <filename>", file=sys.stderr)
#     sys.exit(1)
# ​
# load_memory(sys.argv[1])
# ​
# ​
# while running:
#     # Do stuff
#     command = memory[pc]
# ​
#     if command == PRINT_BEEJ:
#         print("Beej!")
#         pc += 1
# ​
#     elif command == PRINT_NUM:
#         num = memory[pc + 1]
#         print(num)
#         pc += 2
# ​
#     elif command == HALT:
#         running = False
#         pc += 1
# ​
#     elif command == SAVE:
#         num = memory[pc+1]  # Get the num from 1st arg
#         reg = memory[pc+2]  # Get the register index from 2nd arg
#         register[reg] = num # Store the num in the right register
#         pc += 3
# ​
#     elif command == PRINT_REGISTER:
#         reg = memory[pc+1]   # Get the register index from 1st arg
#         print(register[reg]) # Print contents of that register
#         pc += 2
# ​
#     elif command == ADD:
#         reg_a = memory[pc+1]   # Get the 1st register index from 1st arg
#         reg_b = memory[pc+2]   # Get the 2nd register index from 2nd arg
#         register[reg_a] += register[reg_b] # Add registers, store in reg_a
#         pc += 3
# ​
#     else:
#         print(f"Unknown instruction: {command}")
#         sys.exit(1)

#*********************************************************************************
#Day three
# import sys
# ​
# PRINT_BEEJ     = 1
# HALT           = 2
# PRINT_NUM      = 3
# SAVE           = 4  # SAVE VALUE INTO REGISTER
# PRINT_REGISTER = 5
# ADD            = 6
# PUSH           = 7
# POP            = 8
# ​
# ​
# # 256 bytes of memory
# memory = [0] * 32
# ​
# # Create 8 registers, 1 byte each
# register = [0] * 8
# ​
# SP = 7  # Stack pointer is register R7
# ​
# ​
# ​
# pc = 0
# running = True
# ​
# ​
# def load_memory(filename):
#     try:
#         address = 0
# ​
#         with open(filename) as f:
#             for line in f:
#                 # Process comments:
#                 # Ignore anything after a # symbol
#                 comment_split = line.split("#")
# ​
#                 # Convert any numbers from binary strings to integers
#                 num = comment_split[0].strip()
#                 try:
#                     val = int(num)
#                 except ValueError:
#                     continue
# ​
#                 memory[address] = val
#                 address += 1
#                 # print(f"{val:08b}: {val:d}")
# ​
#     except FileNotFoundError:
#         print(f"{sys.argv[0]}: {sys.argv[1]} not found")
#         sys.exit(2)
# ​
# ​
# ​
# if len(sys.argv) != 2:
#     print("usage: simple.py <filename>", file=sys.stderr)
#     sys.exit(1)
# ​
# load_memory(sys.argv[1])
# ​
# ​
# while running:
# ​
#     # print(memory)
# ​
#     # Do stuff
#     command = memory[pc]
# ​
#     if command == PRINT_BEEJ:
#         print("Beej!")
#         pc += 1
# ​
#     elif command == PRINT_NUM:
#         num = memory[pc + 1]
#         print(num)
#         pc += 2
# ​
#     elif command == HALT:
#         running = False
#         pc += 1
# ​
#     elif command == SAVE:
#         num = memory[pc+1]  # Get the num from 1st arg
#         reg = memory[pc+2]  # Get the register index from 2nd arg
#         register[reg] = num # Store the num in the right register
#         pc += 3
# ​
#     elif command == PRINT_REGISTER:
#         reg = memory[pc+1]   # Get the register index from 1st arg
#         print(register[reg]) # Print contents of that register
#         pc += 2
# ​
#     elif command == ADD:
#         reg_a = memory[pc+1]   # Get the 1st register index from 1st arg
#         reg_b = memory[pc+2]   # Get the 2nd register index from 2nd arg
#         register[reg_a] += register[reg_b] # Add registers, store in reg_a
#         pc += 3
# ​
# ​
#     elif command == PUSH:
#         reg = memory[pc + 1]
#         val = register[reg]
#         # Decrement the SP.
#         register[SP] -= 1
#         # Copy the value in the given register to the address pointed to by SP.
#         memory[register[SP]] = val
#         pc += 2
# ​
#     elif command == POP:
#         reg = memory[pc + 1]
#         val = memory[register[SP]]
#         # Copy the value from the address pointed to by SP to the given register.
#         register[reg] = val
#         # Increment SP.
#         register[SP] += 1
#         pc += 2


# ​
# ​
#     else:
#         print(f"Unknown instruction: {command}")
#         sys.exit(1)