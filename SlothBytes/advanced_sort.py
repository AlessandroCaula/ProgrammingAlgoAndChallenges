###################
## Advanced Sort ##
###################

# Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sub lists. Items of the same value should be in the same sub list.
#
# Example:
#
#advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]
#
#advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]
#
#advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]

def advanced_sort(arr):
    # Loop through all the elements in the array.
    dict = {}
    for i, el in enumerate(arr):
        print(i, " ", el)
        if str(el) not in dict.keys():
            dict[str(el)] = [el]
        else:
            dict[str(el)].append(el)
    advanced_sorted_array = list(dict.values())
    return advanced_sorted_array

array_to_sort = [2, 2, 3, 2, 2, 1, 1]
array_to_sort1 = [2, 1, 2, 1]
array_to_sort2 = [5, 4, 5, 5, 4, 3]
array_to_sort3 = ["b", "a", "b", "a", "c"]
print("Advanced Sorting result: ", advanced_sort(array_to_sort3))