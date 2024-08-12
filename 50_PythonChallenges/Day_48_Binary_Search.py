# Day 48

## Binary Search 

'''
Write a function called search_binary that searches for the number 22 in the following list and returns its index. 
The function should take two parameters, the list and the item that is being searched for. Use binary search (iterative Method).

list = [12, 34, 56, 78, 98, 22, 45, 13]
'''

def search_binary(list, num):
    # First sort the list.
    list = sorted(list)
    start = 0
    end = len(list) - 1
    while start > 0 or end < len(list):
        i = (end + start) // 2
        if list[i] == num:
            return f"The element index is: {i}" 
        else:
            if num < list[i]:
                end = i - 1
            else:
                start = i + 1
    return "Element Not found"

list = [12, 34, 56, 78, 98, 22, 45, 13]
num = 22
print(search_binary(list, num))