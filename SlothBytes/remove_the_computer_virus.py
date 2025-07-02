###############################
## Remove the Computer Virus ##
###############################

# You computer might have been infected by a virus! Create a function that finds the viruses in files and removes them from you computer
#
# remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")
# output = "PC Files: spotifysetup.exe, dog.jpg"

# remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")
# output = "PC Files: antivirus.exe, cat.pdf"

# remove_virus("PC Files: notvirus.exe, funnycat.gif")
# output = "PC Files: notvirus.exe, funnycat.gif")

# Notes: 
# - Bad files will contains "virus" or "malware", but "antivirus" and "notvirus" will no be viruses. 
# - Return "PC Files: Empty" if there are no files left on the computer. 

def remove_virus(pc_files):
    # First split the PC_file string. 
    pc_file_split = pc_files.split(":");
    files_list = pc_file_split[1].split(",")
    pc_file_cleaned = "";
    # Loop through all the word in the pc_file_split
    for w in files_list:

        # Then split each word by the ".". If it exists the first word is the file name.
        w_split = w.split(".")

        # Check if in the "virus" word is included, and if it is different from "anitivirus" and "notvirus"
        if len(w_split) != 0 and ("virus" in w_split[0] or "malware" in w_split[0]) and (w_split[0][1:] != "antivirus" and w_split[0][1:] != "notvirus"):
            print("Virus found: ", w_split[0] + "." + w_split[1], " ...Deleting")
        else:
            # If it is not a virus, then leave it in the File directory.
            pc_file_cleaned += ".".join(w_split)

    return "Cleaned directory: \n" + (pc_file_split[0] + ":" + pc_file_cleaned if pc_file_cleaned != "" else pc_file_split[0] + ": " + "Empty")
            

            
    return True

print(remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe "))
print(remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg"))
print(remove_virus("PC Files: notvirus.exe, funnycat.gif"))
print(remove_virus("PC Files: virus.exe, lethalmalware.jpg"))