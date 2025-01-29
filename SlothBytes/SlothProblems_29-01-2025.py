##################
## Amateur Hour ##
##################

# Write a function that takes time t1 and time t2 and returns the number of hours passed between thw two times

# Examples
# 
# hoursPassed("3:00 AM", "9:00 AM")
# output = "6 hours"
# 
# hoursPassed("2:00 PM", "4:00 PM")
# output = "2 hours"

# hoursPassed("1:00 AM", "3:00 PM")
# output = "14 hours"

# hoursPassed("4:00 PM", "4:00 PM")
# output = "no time passed"

def hours_passed(start:str, end:str):
    # Split the start and end times
    start_split = start.split(" ")
    end_split = end.split(" ")
    # First retrieve if the hour is AM or PM
    meridian_start = start_split[1]
    meridian_end = end_split[1]
    # Retrieve the hours and the minutes
    start_hour = start_split[0].split(":")[0]
    start_minute = start_split[0].split(":")[1]
    end_hours = end_split[0].split(":")[0]
    end_minute = end_split[0].split(":")[1]

    # Convert hours in integers
    start_hour_int = int(start_hour) if start_hour.isdigit() else -1
    end_hour_int = int(end_hours) if end_hours.isdigit() else -1
    start_minute_int = int(start_minute) if start_minute.isdigit() else -1
    end_minute_int = int(end_minute) if end_minute.isdigit() else -1
    if start_hour_int == -1 or end_hour_int == -1 or start_minute_int == -1 or end_minute_int == -1: 
        return "Invalid hour"
    # If one of the two hours (start and/or end) are in PM, add 12 to their hours
    start_hour_int = start_hour_int + 12 if meridian_start == "PM" else start_hour_int
    end_hour_int = end_hour_int + 12 if meridian_end == "PM" else end_hour_int
    
    # Convert the hours in minutes 
    start_tot_minutes = start_minute_int + (start_hour_int * 60)
    end_tot_minutes = end_minute_int + (end_hour_int * 60)
    # Subtract the end and start total minutes
    difference_tot_minutes = end_tot_minutes - start_tot_minutes
    # Ri-convert the difference minutes in hours
    difference_hours = difference_tot_minutes // 60
    difference_minutes = difference_tot_minutes - (difference_hours * 60)
    # Compute the final time that has passed between the start and end hours
    time_passed = ("0" if len(str(difference_hours)) == 1 else "") + str(difference_hours) + ":" + ("0" if len(str(difference_minutes)) == 1 else "") + str(difference_minutes)

    return time_passed

print(hours_passed("1:00 AM", "3:00 PM"))
print(hours_passed("2:50 AM", "3:10 AM"))
print(hours_passed("3:50 AM", "4:20 PM"))