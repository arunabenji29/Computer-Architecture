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
