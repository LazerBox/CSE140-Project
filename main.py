# Global variables
pc = 0
instructions = []  # We'll load the program.txt here
registers = [0] * 32  # 32 registers

# Decoding info moved from machine_to_binary
instruction_set = {
    "0110011": "R",
    "0000011": "I",
    "0001111": "I",
    "0010011": "I",
    "1100111": "I",
    "0100011": "S",
    "1100011": "SB",
    "1101111": "UJ"  # UJ only has jal
}

r_instructions = {
    ("000", "0000000"): "add",
    ("000", "0100000"): "sub",
    ("111", "0000000"): "and",
    ("110", "0000000"): "or"
}

i_instructions = {
    "000": "lw",
    "111": "andi",
    "110": "ori",
    "000": "addi"
}

sb_instructions = {
    "000": "beq"
}

s_instructions = {
    "010": "sw"
}

def load_program(file_name):
    global instructions
    with open(file_name, 'r') as f:
        instructions = [line.strip() for line in f.readlines()]

def Fetch():
    global pc
    if pc // 4 >= len(instructions):
        print("End of program!")
        return None
    instruction = instructions[pc // 4]
    print(f"Fetched instruction at PC={pc}: {instruction}")
    pc += 4
    return instruction

def Decode(instruction):
    print(f"Decoding instruction: {instruction}")
    
    opcode = instruction[-7:]
    instr_type = instruction_set.get(opcode, None)
    
    if instr_type is None:
        print("Unknown instruction type!")
        return None
    
    if instr_type == "R":
        rd = int(instruction[20:25], 2)
        funct3 = instruction[17:20]
        rs1 = int(instruction[12:17], 2)
        rs2 = int(instruction[7:12], 2)
        funct7 = instruction[0:7]
        operation = r_instructions.get((funct3, funct7), "Unknown")
        decoded = {"type": "R", "operation": operation, "rd": rd, "rs1": rs1, "rs2": rs2}
    
    elif instr_type == "I":
        rd = int(instruction[20:25], 2)
        funct3 = instruction[17:20]
        rs1 = int(instruction[12:17], 2)
        imm = int(instruction[0:12], 2)
        operation = i_instructions.get(funct3, "Unknown")
        decoded = {"type": "I", "operation": operation, "rd": rd, "rs1": rs1, "imm": imm}
    
    elif instr_type == "S":
        funct3 = instruction[17:20]
        rs1 = int(instruction[12:17], 2)
        rs2 = int(instruction[7:12], 2)
        imm = int(instruction[0:7] + instruction[20:25], 2)
        operation = s_instructions.get(funct3, "Unknown")
        decoded = {"type": "S", "operation": operation, "rs1": rs1, "rs2": rs2, "imm": imm}
    
    elif instr_type == "SB":
        funct3 = instruction[17:20]
        rs1 = int(instruction[12:17], 2)
        rs2 = int(instruction[7:12], 2)
        imm = int(instruction[0] + instruction[24] + instruction[1:7] + instruction[20:24] + '0', 2)
        operation = sb_instructions.get(funct3, "Unknown")
        decoded = {"type": "SB", "operation": operation, "rs1": rs1, "rs2": rs2, "imm": imm}
    
    elif instr_type == "UJ":
        rd = int(instruction[20:25], 2)
        imm = int(instruction[0] + instruction[12:20] + instruction[11] + instruction[1:11] + '0', 2)
        decoded = {"type": "UJ", "operation": "jal", "rd": rd, "imm": imm}
    
    else:
        print("Unknown instruction format!")
        decoded = None

    print(f"Decoded: {decoded}")
    return decoded

def Execute(decoded_instruction):
    print(f"Executing: {decoded_instruction}")
    # Placeholder for ALU ops

def Memory(decoded_instruction):
    print(f"Memory Access: {decoded_instruction}")
    # Placeholder for memory ops

def Writeback(decoded_instruction):
    print(f"Writeback: {decoded_instruction}")
    # Placeholder for register file update

def main():
    print("Welcome to RISC-V CPU Simulator")
    filename = input("Enter the program file name (example: sample_part1.txt): ")
    load_program(filename)

    while True:
        print("\nOptions:")
        print("1. Fetch")
        print("2. Decode")
        print("3. Execute")
        print("4. Memory")
        print("5. Writeback")
        print("6. Run Next Instruction (all stages)")
        print("7. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            instr = Fetch()
        elif choice == "2":
            instr = Fetch()
            decoded = Decode(instr)
        elif choice == "3":
            instr = Fetch()
            decoded = Decode(instr)
            Execute(decoded)
        elif choice == "4":
            instr = Fetch()
            decoded = Decode(instr)
            Execute(decoded)
            Memory(decoded)
        elif choice == "5":
            instr = Fetch()
            decoded = Decode(instr)
            Execute(decoded)
            Memory(decoded)
            Writeback(decoded)
        elif choice == "6":
            instr = Fetch()
            if instr:
                decoded = Decode(instr)
                if decoded:
                    Execute(decoded)
                    Memory(decoded)
                    Writeback(decoded)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()