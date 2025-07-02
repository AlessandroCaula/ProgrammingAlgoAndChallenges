###########################
# Video Length in Seconds #
###########################

# You are given the length of a video in minutes. The format is mm:ss (ex: "02:54")
# Create a function that takes the video length and return it in seconds. 

### Examples
# minutesToSeconds("01:00") = 60
# 
# minutesToSeconds("13:56") = 836
# 
# minutesToSeconds("10:60") = -1
# 
# minuteToSeconds("121:49") = 7309

# - If the number of seconds is 60 or over, return -1 (see example 3).
# - You may get a number of minutes over 99 (see example 4).

def minutesToSeconds(length_string = str):
    length_split = length_string.split(":")
    if int(length_split[1]) >= 60:
        return -1 
    total_length_sec = (int(length_split[0]) * 60) + int(length_split[1])
    return f'{total_length_sec}'

print(minutesToSeconds("01:00"))
print(minutesToSeconds("13:56"))
print(minutesToSeconds("10:60"))
print(minutesToSeconds("121:49"))