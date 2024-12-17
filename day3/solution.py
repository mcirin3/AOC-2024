import re 

def sum_valid_muls(memory):
    with open(file_path, 'r') as file:
        memory = file.read()
    #the regular expressure to match the valid expresion 
    pattern =  r"mul\((\d+),(\d+)\)"
    
    #find all matches in the memory string 
    matches=re.findall(pattern, memory)
    #initalize the total sum
    total_sum = 0
    #iterate through matches and calulate result of each mul
    for x,y in matches:
        total_sum += int(x) * int(y)
    return total_sum

def sum_valid_muls_with_conditions(file_path):
    # Read the corrupted memory from the file
    with open(file_path, 'r') as file:
        memory = file.read()
    
    # Regular expressions to match the instructions
    mul_pattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"(do\(\)|don't\(\))"
    
    # Find all instructions in the memory
    instructions = re.findall(f"{control_pattern}|{mul_pattern}", memory)
    
    # Track whether mul instructions are enabled (default is enabled)
    mul_enabled = True
    total_sum = 0

    # Iterate through instructions
    for inst in instructions:
        # Check if it's a control instruction
        if inst[0] == "do()":
            mul_enabled = True
        elif inst[0] == "don't()":
            mul_enabled = False
        # Check if it's a mul instruction and apply if enabled
        elif inst[1] and inst[2]:  # Matches `mul(X, Y)`
            if mul_enabled:
                x, y = int(inst[1]), int(inst[2])
                total_sum += x * y
    
    return total_sum

file_path = "input.txt"
file_path2 = "input2.txt"
result = sum_valid_muls(file_path)
result2 = sum_valid_muls_with_conditions(file_path2)
print("Sum of valid multiplications: ", result)
print("Sum of valid multiplications with rules: ", result2)
    