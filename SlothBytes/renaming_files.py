import argparse
import os

def renaming(input_dir):
    # List all the files present in the directory
    files = os.listdir(input_dir)
    # Create a txt that will keep track of the new title and the date of the exercise
    with open("title_to_date.txt", "w") as file_to_date:
        for file_name in files:
            read_file = open(file_name, mode="r")

            # Avoid renaming this file
            if file_name == "renaming_files.py":
                continue
            # For the moment do not parse the Jupiter Notebook files (".ipynb")
            if file_name.split('.').pop() == "ipynb":
                continue
            # Do not change the title if it is not a python file
            if file_name.split('.')[1] != "py":
                continue
            
            # Retrieve the date of the exercise
            date = file_name.split("_").pop().split(".")[0]
            # Retrieve the exercise from inside the file and add the date inside the exercise
            new_filename = retrieve_file_title(read_file)

            # If the file is the new_filename is None. Don't change the false
            if new_filename == None:
                continue

            new_filename = new_filename.lower().strip().replace(" ", "_") + ".py"
            for ch in [',', '+', '#', '!', '?']:
                new_filename = new_filename.replace(ch, "")
            new_filename = new_filename.replace("/", "-")
            
            # Store the filename and the date in the txt file
            file_to_date.write(f'{new_filename} -> {date}\n')

            # Renaming the file
            os.rename(file_name, new_filename)


# Function that will return the title of the file
def retrieve_file_title(read_file):
    save_title = False
    # Loop through all the lines of the file
    for line in read_file:
        if save_title:
            line = line.replace("#", "").rstrip()
            read_file.close()
            return line
        if '####' in line:
            save_title = not save_title

    # If title is found, return None
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Renaming files script")

    parser.add_argument(
        "--input_dir",
        default="./",
        help="Directory with files with rename (by default ./)"
    )

    args = parser.parse_args()
    input_dir = args.input_dir

    # Call the main renaming function
    renaming(input_dir)