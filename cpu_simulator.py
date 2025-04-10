
# Global variables
pc = 0
instructions = []  # We'll load the program.txt here
registers = [0] * 32  # 32 registers

def load_program(file_name):
    global instructions
    try:
        with open(file_name, 'r') as f:
            instructions = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found. Please check the file path and try again.")
        exit(1)  # Exit the program if the file is not found

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
    # Example placeholder: Actually, you'd split fields and check opcode, funct3, etc.
    return "Decoded Instruction (placeholder)"

def Execute(decoded_instruction):
    print(f"Executing: {decoded_instruction}")
    # Placeholder for ALU ops
    return "Execution Result (placeholder)"

def Mem(decoded_instruction, execution_result):
    print(f"Memory Access for: {decoded_instruction}")
    return "Memory Result (placeholder)"

def Writeback(decoded_instruction, memory_result):
    print(f"Writeback for: {decoded_instruction}")
    # Example: update register file
    pass

def main():
    load_program('sample_part1.txt')  # Load first part
    print("First part loaded. Now loading second part...")
    load_program('sample_part2.txt')  # Load second part

    while True:
        print("\n--- Single-Cycle CPU Simulator ---")
        print("Choose an action:")
        print("1. Fetch Instruction")
        print("2. Decode Instruction")
        print("3. Execute Instruction")
        print("4. Memory Access")
        print("5. Writeback")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            instr = Fetch()
        elif choice == '2':
            if 'instr' in locals():
                decoded = Decode(instr)
            else:
                print("Please Fetch first!")
        elif choice == '3':
            if 'decoded' in locals():
                exec_result = Execute(decoded)
            else:
                print("Please Decode first!")
        elif choice == '4':
            if 'decoded' in locals() and 'exec_result' in locals():
                mem_result = Mem(decoded, exec_result)
            else:
                print("Please Execute first!")
        elif choice == '5':
            if 'decoded' in locals() and 'mem_result' in locals():
                Writeback(decoded, mem_result)
            else:
                print("Please Memory Access first!")
        elif choice == '6':
            print("Exiting CPU Simulator.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
