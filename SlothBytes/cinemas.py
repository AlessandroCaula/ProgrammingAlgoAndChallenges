#############
## Cinemas ##
#############

# 06_08_2025

# Given an array of seats return the maximum number of new people which can be seated, as long as there is at least a gap of 2 seats between people.
# 
# - Empty seats are given as 0
# - Occupied seats are given as 1
# - Don't move any seats which are already occupied, even if they are less than 2 seats apart. Consider only the gaps between new seats and existing seats. 
# 
# EXAMPLES
# 
# maximumSeating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0])
# output = 2
# # [1, 0, 0, 1, 0, 0, 1, 0, 0, 1] 2 new people were seated!
# 
# maximumSeating([0, 0, 0, 0])
# output = 2
# # [1, 0, 0, 1] 2 new people were seated!
#
# maximumSeating([1, 0, 0, 0, 0, 1])
# output = 0
# # There is no way to have a gap of at least 2 chairs when adding someone else.
# 
# maximumSeating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0])
# output = 2
# 
# maximumSeating([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# output = 4

def maximumSeating(seats):
    newPeople = 0
    for i in range(len(seats)):
        # If the current seat is 0 Check the 2 seats before and after the current. 
        if seats[i] == 0:
            # Check for seats before
            freeSeatBefore = True
            for j in range(1, 3):
                if i - j >= 0:
                    # check if there are 1s
                    if seats[i - j] == 1:
                        freeSeatBefore = False
                        break
            # Check for seats after
            freeSeatAfter = True
            for j in range(1, 3):
                if i + j < len(seats):
                    # Check if there are 1s
                    if seats[i + j] == 1:
                        freeSeatAfter = False
                        break
            # If there are free seats, the new person can seat
            if freeSeatBefore and freeSeatAfter:
                newPeople += 1
                seats[i] = 1

    return (newPeople, seats)

print(maximumSeating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]))
print(maximumSeating([0, 0, 0, 0]))
print(maximumSeating([1, 0, 0, 0, 0, 1]))
print(maximumSeating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]))
print(maximumSeating([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))