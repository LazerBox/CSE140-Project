'''
Welcome to our file
'''
#Globals
total_clock_cycles = 0
pc = 0
branch_target = 0
alu_zero = 0
next_pc = 0

d_mem = [0 for _ in range(32)]
rf = [0 for _ in range(32)]

instructions = []

#Functions
def read_file(filename):
    with open(filename, "r") as f:
        instructions = [line.strip() for line in f if line.strip()]


def fetch():
    index = pc // 4

    if index >= len(instructions):
        return None

    instruction = instructions[index]

    next

    return instruction

def decode():
    return 0

def execute(alu_ctrk):
    return 0

def mem(address, lw, sw, data):



    return 0

def writeBack(results, data):



    total_clock_cycles += 1


'''Place Actionable Code Below'''
def main():
    #file_name = input("Enter the program file name to run:\n")
    read_file("sample_part1.txt")


    while instructions:

        instruction = fetch()

        decoded = decode(instruction)





        print(total_clock_cycles)


if __name__ == "__main__":
    main()




'''
Plan to finish
___
___
___
___
___
'''