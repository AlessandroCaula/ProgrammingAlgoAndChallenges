############################
#### Simon Says ############
############################

# Simon asks you to perform operations on a list od numbers that only he tells you. 
# You should ignore all other instructions given. 
# Create a function which evaluates a list of commands (written in plain English) if the command begins with Simon says. Return the result as an integer.

def simon_says():
    final_result = 0
    while True:
        # Get the input from the user
        operation_instruction = input('- ').lower()

        # If the name simon is not included in the operation instruction, don't perform it 
        if "simon" not in operation_instruction:
            print("Error: Not a Simon request")
            continue
        # If the operation instruction ask for the result, exit from the loop and return the final total.
        elif ('result' or 'equal' or 'total') in operation_instruction:
            break        
        else:
            # Retrieve the number present in the instruction.
            operation_number = int([el for el in operation_instruction.split(" ") if el.isnumeric()][0])
            # Check which operation has to be performed
            if "add" in operation_instruction or "sum" in operation_instruction:
                final_result += operation_number
            elif "subtract" in operation_instruction or "minus" in operation_instruction:
                final_result -= operation_number
            elif "multiply" in operation_instruction:
                final_result *= operation_number
            elif "divide" in operation_instruction:
                final_result /= operation_number
            else:
                print("Error: Invalid operation")
    
    # Return the final result. 
    return f'\nYour final result is: {final_result}'


print(simon_says())