###########################
## What Gives a Bad Mood ##
###########################
#
# 13-08-2025
# 
# Let's say the greatest impact on someone's mood are: weather, meals, and sleep.
# Your task is, given an array of sub-arrays of different values for:
# 
# [Mood, Weather, Meals, Sleep]
# 
# All values except for meals are 1-10 (1 = bad, 10 = good)
# Meals are from 1-3
# 
# Determine which other variable has had the greatest impact on the mood
# 
# 
# EXAMPLES
# 
# greatestImpact([
#   [1, 1, 3, 10],
#   [1, 1, 3, 10],
#   [1, 1, 3, 10]
# ])
# output = "Weather"
# # Weather was always low but all others were high.

# greatestImpact([
#   [10, 10, 3, 10],
#   [10, 10, 3, 10],
#   [10, 10, 3, 10]
# ])
# output = "Nothing"

# # Great days! all values were high.

# greatestImpact([
#   [8, 9, 3, 10],
#   [2, 10, 1, 9],
#   [1, 9, 1, 8]
# ])
# output = "Meals"

# greatestImpact([
#   [10, 9, 3, 9],
#   [1, 8, 3, 4],
#   [10, 9, 2, 8],
#   [2, 9, 3, 2]
# ])
# output = "Sleep"

def greatest_impact(days: list[list[int]]) -> str:
    moods = ["Weather", "Meals", "Sleep"]
    mood_values = {
        "Weather": 0,
        "Meals": 0,
        "Sleep": 0,
    }

    for day in days:
        if day[0] == 10:
            continue
        else:
            more_impact_value = ''
            perc_value = 2
            # find the greatest impact
            for i, val in enumerate(day[1:]):
                if moods[i] == "Meals":
                    perc_local = val / 3
                else:
                    perc_local = val / 10
                
                # Check if it is lower than the perc_value
                if perc_local < perc_value:
                    perc_value = perc_local
                    more_impact_value = moods[i]
            
        mood_values[more_impact_value] += 1
    
    print(mood_values)

    return max(mood_values.items(), key=lambda item: item[1])[0] if max(mood_values.items(), key=lambda item: item[1])[1] != 0 else "Nothing"



days = [
  [8, 9, 3, 10],
  [2, 10, 1, 9],
  [1, 9, 1, 8]
]

print(greatest_impact(days))

days = [
  [10, 9, 3, 9],
  [1, 8, 3, 4],
  [10, 9, 2, 8],
  [2, 9, 3, 2]
]

print(greatest_impact(days))

days = [
  [10, 10, 3, 10],
  [10, 10, 3, 10],
  [10, 10, 3, 10]
]

print(greatest_impact(days))

days = [
  [1, 1, 3, 10],
  [1, 1, 3, 10],
  [1, 1, 3, 10]
]

print(greatest_impact(days))