import re

with open("17/data.txt", "r") as file:
    data = file.read()

# Extract register values
registers = re.findall(r'Register [A-C]: (\d+)', data)
registers = list(map(int, registers))

reg_A = registers[0]
reg_B = registers[1]
reg_C = registers[2]

# Extract program values
program = re.findall(r'Program: ([\d,]+)', data)
program = list(map(int, program[0].split(',')))

# * Part 1


def get_operand_value(operand, reg_A, reg_B, reg_C):
    if operand <= 3:
        return operand
    elif operand == 4:
        return reg_A
    elif operand == 5:
        return reg_B
    elif operand == 6:
        return reg_C
    else:
        raise ValueError("Invalid operand")


output = []
instruction_pointer = 0

while instruction_pointer < len(program):
    opcode = program[instruction_pointer]
    operand = program[instruction_pointer + 1]

    if opcode == 0:  # adv
        reg_A //= 2 ** get_operand_value(operand, reg_A, reg_B, reg_C)
    elif opcode == 1:  # bxl
        reg_B ^= operand
    elif opcode == 2:  # bst
        reg_B = get_operand_value(operand, reg_A, reg_B, reg_C) % 8
    elif opcode == 3:  # jnz
        if reg_A != 0:
            instruction_pointer = operand
            continue
    elif opcode == 4:  # bxc
        reg_B ^= reg_C
    elif opcode == 5:  # out
        output.append(str(get_operand_value(operand, reg_A, reg_B, reg_C) % 8))
    elif opcode == 6:  # bdv
        reg_B = reg_A // 2 ** get_operand_value(operand, reg_A, reg_B, reg_C)
    elif opcode == 7:  # cdv
        reg_C = reg_A // 2 ** get_operand_value(operand, reg_A, reg_B, reg_C)
    else:
        raise ValueError("Invalid opcode")

    instruction_pointer += 2

res = ",".join(output)
print(res)
