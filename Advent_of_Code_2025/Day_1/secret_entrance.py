import argparse
import math

def secret_entrance_part1(input_path: str):
    input_sequence = open(input_path)
    pointer = 50
    number_of_zeros = 0

    for line in input_sequence:
        # Get the direction of the rotation
        line = line.strip()
        direction = line[0]
        # Compute the modal, so to avoid entire rotations
        steps = int(line[1:]) % 100

        if (direction == "L"):                
            # Go left, to the lower numbers
            pointer -= steps
            # If it goes negative, then subtract to 100
            if pointer < 0:
                # Subtract to the pointer
                pointer = 100 + pointer
        else:
            # Go right, to the highest numbers
            pointer += steps
            # If it goes over 99, then restart from 0
            if pointer > 99:
                pointer = 0 + (pointer - 100)
        
        # Increment final number times the dial point to the 0
        if pointer == 0: number_of_zeros += 1

    input_sequence.close()
    return number_of_zeros

def secret_entrance_part2(input_path: str):
    input_sequence = open(input_path)
    pointer = 50
    number_of_zeros = 0

    for line in input_sequence:
        # Get the direction of the rotation
        line = line.strip()
        direction = line[0]
        steps = int(line[1:])
        # Compute the number of times that the pointer passes through the 0 when a full rotation is done
        full_rotation = math.floor(steps / 100)
        # Add the full rotations to the number_of_zeros following the method 0x434C49434B
        number_of_zeros += full_rotation
        # Compute the modal, so to avoid entire rotations
        steps = steps % 100

        # Retrieve the starting point of the pointer
        prev_pointer = pointer

        if (direction == "L"):                
            # Go left, to the lower numbers
            pointer -= steps
            # If it goes negative, then subtract to 100
            if pointer < 0:
                # Subtract to the pointer
                pointer = 100 + pointer
                if pointer != 0 and prev_pointer != 0:
                    # Increment by 1 the number of zeros
                    number_of_zeros += 1
        else:
            # Go right, to the highest numbers
            pointer += steps
            # If it goes over 99, then restart from 0
            if pointer > 99:
                pointer = 0 + (pointer - 100)
                if pointer != 0 and prev_pointer != 0:
                    # Increment by 1 the number of zeros
                    number_of_zeros += 1
        
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

    # Part 1 result
    part_1_res = secret_entrance_part1(input_path)
    print("Part 1: ", part_1_res)

    # Part 2 result
    part_2_res = secret_entrance_part2(input_path)
    print("Part 2: ", part_2_res)


if __name__ == "__main__":
    main() 