####################
## Bridge Shuffle ##
####################

# Create a function to bridge shuffle two arrays.
# To bridge shuffle, you interleave the elements from both arrays in an alternating fashion:

# Example 1:
# 
# array1 = ["A", "A", "A"]
# array2 = ["B", "B", "B"]
# shuffled_array = ["A", "B", "A", "B", "A", "B"]

# This can still work with two array of uneven length. We simply tack on the extra elements from the longer array.
# 
# array1 = ["C", "C", "C", "C"]
# array2 = ["D"]
# shuffled_array = ["C", "D", "C", "C", "C"]

def bridge_shuffle1(array1: list, array2: list): 
    final_array = []
    i = 0
    j = 0
    for z in range(len(array1) + len(array2)):
        if (i > len(array1)):
            final_array.append(array2[j])
            j += 1
        elif (z % 2 == 0):
            final_array.append(array1[i])
            i += 1
        elif (j > len(array2)):
            final_array.append(array1[i])
            i += 1
        elif (z % 2 != 0):
            final_array.append(array2[j])
            j += 1

    return final_array


def bridge_shuffle(array1: list, array2: list): 
    final_array = []
    i = 0
    j = 0    
    for z in range(len(array1) + len(array2)):
        if (i < len(array1) or j < len(array2)):
            if (z % 2 == 0):
                final_array.append(array1[i])
                i += 1
            else:
                final_array.append(array2[j])
                j += 1
        else:
            if (i < len(array1)):
                final_array.append(array1[i])
                i += 1
            elif (j < len(array2)):
                final_array.append(array2[j])
                j += 1

    return final_array

array1 = ["A", "A", "A"]
array2 = ["B", "B", "B"]
print(bridge_shuffle(array1, array2))

# array1 = ["C", "C", "C", "C"]
# array2 = ["D"]
# print(bridge_shuffle(array1, array2))