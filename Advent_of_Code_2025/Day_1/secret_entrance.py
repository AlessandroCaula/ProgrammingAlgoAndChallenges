import argparse

# def secret_entrance(input_path: str):
#     input_sequence = open(input_path)
#     pointer = 50
#     number_of_zeros = 0
#     for line in input_sequence:
#         # Get the direction of the rotation
#         line = line.strip()
#         direction = line[0]
#         steps = int(line[1:])

#         if (direction == "L"):
#             # Go left, to the lower numbers
#             pointer -= steps
#             # If it goes negative, then subtract to 99
#             if pointer < 0:
#                 # Subtract to the pointer
#                 pointer = 100 + pointer
#         else:
#             # Go right, to the highest numbers
#             pointer += steps
#             # If it goes over 99, then restart from 0
#             if pointer > 99:
#                 pointer = 0 + (pointer - 100)
        
#         # Increment final number times the dial point to the 0
#         if pointer == 0: number_of_zeros += 1

#     input_sequence.close()
#     return number_of_zeros

def secret_entrance(input_path: str):
    input_sequence = open(input_path)
    pointer = 50
    number_of_zeros = 0

    # print(99 % 99)

    for line in input_sequence:
        # Get the direction of the rotation
        line = line.strip()
        direction = line[0]
        steps = int(line[1:]) % 100

        if (direction == "L"):                
            # Go left, to the lower numbers
            pointer -= steps
            # If it goes negative, then subtract to 99
            if pointer < 0:
                # Subtract to the pointer
                pointer = 100 + pointer
        else:
            # Go right, to the highest numbers
            pointer += steps
            # If it goes over 99, then restart from 0
            if pointer > 99:
                pointer = 0 + (pointer - 100)
        # print(pointer)
        
        # Increment final number times the dial point to the 0
        if pointer == 0: number_of_zeros += 1

    input_sequence.close()
    return number_of_zeros
        
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input",
        help="Path to input file"
    )
    args = parser.parse_args()
    input_path = args.input
    print(secret_entrance(input_path))

if __name__ == "__main__":
    main() 