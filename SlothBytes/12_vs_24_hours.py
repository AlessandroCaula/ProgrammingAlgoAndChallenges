######################
### 12 vs 24 Hours ###
######################
#
# Create a function that converts 12-hours time to 24-hours time or vice-versa. Return the output as a string. 
#
# convertTime("12:00 am")
# output = "00:00"
#
# convertTime("6:20 pm")
# output = "18:20"
#
# convertTime("21:00")
# output = "9:00 pm"
#
# convertTime("5:05")
# output ="5:05 am"
#
# Notes
#
# - A 12-hours time input will be denoted with an "am" or "pm" suffix.
# - A 24-hours input time contains no suffix.

# 12:00 am --> 00:00


def convertTime(time: str):
    output_time = ""
    time_split = time.split(" ")
    
    # Extract the hours. Convert it to string. Chatch ValueError if the string cannot be converted to int. 
    try: 
        hours = int(time_split[0].split(":")[0])
    except ValueError:
        print("Time is not a number")
        
    # If the time_split array is longer than 1, means that the time has been given with the "am" or "pm". Therefore we have to convert it to 24-hours format. 
    if len(time_split) > 1:
        # Check if the suffix is "am" or "pm"
        # If the time has been given with a "pm" suffix, we have to rewrite the output time by adding 12 to the hours.
        if time_split[1] == "pm":               
            # if is 12:00 pm, midday, then return as it is. Otherwise add 12 to the hours in order to convert it to 24-hours format
            output_time = (str(hours) if str(hours) == "12" else str(hours + 12)) + ":" + time_split[0].split(":")[1]
        else:
            # If hours is 12 am (midnight) then the 24-hours format will be 00:mm. Otherwise leave at it is.
            output_time = ("00" if str(hours) == "12" else str(hours)) + ":" + time_split[0].split(":")[1]
    # Otherwise we have to convert the time from 24-hours format to 12-hours format 
    else:
        # if the hour is greater than 12 sutract 12 to it.
        if hours >= 12:
            # Check if it is midday (12:00) which is converted to 12:00 pm. Then leave the 12 without subtracting anything. 
            output_time = (str(hours) if str(hours) == "12" else str(hours - 12)) + ":" + time_split[0].split(":")[1] + " " + "pm"
        else:
            output_time = ("12" if str(hours) == "0" else str(hours)) + ":" + time_split[0].split(":")[1] + " " + "am"     

    return output_time  
            
    
print(convertTime("12:00 am"))
print(convertTime("12:00 pm"))
print(convertTime("00:00"))
print(convertTime("12:00"))
print()
print(convertTime("12:00 am"))
print(convertTime("6:20 pm"))
print(convertTime("21:00"))
print(convertTime("5:05"))
