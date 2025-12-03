# You're setting an alarm for the next morning an know how long you want to sleep.
# Your job is to figure out what time you need to go to bed to get that amount of sleep.

# Each input has two parts:
# 1. The alarm time *when you'll wake up).
# 2 The sleep duration (how long you want to sleep)

# Return the time you should go to bed — in 24-hour format ("HH:MM").

# bedTime(["07:50", "07:50"])
# output = ["00:00"]

# bedTime(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"])
# output = ["20:15", "22:00", "23:30"]

# bedTime(["05:45", "04:00"], ["07:10", "04:30"])
# output = ["01:45", "02:40"]

import math


def bed_time(times: list[str]) -> list[str]:

    def convert_time_to_hour(difference_min):
        hour = math.floor(difference_min / 60)
        minutes = difference_min - (hour * 60)
        # Converting to string 
        hour_str = str(hour) if len(str(hour)) == 2 else "0" + str(hour)
        minutes_str = str(minutes) if len(str(minutes)) == 2 else "0" + str(minutes)
        return hour_str + ":" + minutes_str

    times_to_bed_final = []
    for wake_up_str, sleep_duration_str in times:
        print(wake_up_str, sleep_duration_str)

        # Convert to string times to integers in minutes
        wake_up_min = (int(wake_up_str.split(":")[0]) * 60) + int(
            wake_up_str.split(":")[1]
        )
        sleep_duration_min = (int(sleep_duration_str.split(":")[0]) * 60) + int(
            sleep_duration_str.split(":")[1]
        )

        # Now subtract the time to sleep to the wake up time
        difference_min = wake_up_min - sleep_duration_min

        # If the difference is positive, means that we can go to sleep after midnight, just convert the minutes to hours
        time_to_bed = ""
        if difference_min >= 0:
            times_to_bed_final.append(convert_time_to_hour(difference_min))
        else:
            # Means that we have to go to bed before midnight, so subtract the difference to midnight
            difference_min = (24 * 60) + difference_min
            print(difference_min)
            times_to_bed_final.append(convert_time_to_hour(difference_min))

    print(times_to_bed_final)


bed_time([["06:15", "10:00"], ["05:45", "04:00"], ["07:50", "07:50"]])
