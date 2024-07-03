# Binary Search - Recursive
list = [1, 2, 3, 4, 5, 6, 7, 8]
num_to_find = 2

print("Binary Search Recursive")

def binarySearchRecursive(list, num_to_find):
    idx_middle = len(list) // 2
    if list[idx_middle] == num_to_find:
        return print("Found")
    elif len(list) == 1:
        return print("NOT Found", -1)
    else: 
        if num_to_find < list[idx_middle]:
            binarySearchRecursive(list[:idx_middle], num_to_find)
        elif num_to_find > list[idx_middle]:   
            binarySearchRecursive(list[idx_middle + 1:], num_to_find)

binarySearchRecursive(list, num_to_find)


print()
print("Binary Search Recursive With Idx")

def binarySearchRecursiveWithIdx(list, begin, end, num_to_find):
    middle = begin + (end - begin) // 2
    if middle == len(list):
        return print("Not Found", -1)
    if list[middle] == num_to_find:
        return print("Found at Idx: ", middle)
    if middle == 0:
        return print("NOT Found", -1)
    else:
        if num_to_find < list[middle]:
            binarySearchRecursiveWithIdx(list, 0, middle, num_to_find)
        elif num_to_find > list[middle]:
            binarySearchRecursiveWithIdx(list, middle + 1, len(list), num_to_find)


binarySearchRecursiveWithIdx(list, 0, len(list) - 1, num_to_find)


print()
print("Binary Search Recursive With Idx GeeksForGeeks")

def binarySearchRecursiveWithIdxGeeksForGeeks(list, begin, end, num_to_find):
    #Check base case
    if end >= begin:
        mid = begin + (end - begin) // 2

        # If the element is present at the middle itself
        if list[mid] == num_to_find:
            return print("Found at idx:", mid)

        # If element is smaller than min, then it can only be present in the left subarray
        elif list[mid] > num_to_find:
            return binarySearchRecursiveWithIdxGeeksForGeeks(list, begin, mid - 1, num_to_find)
        # Else the element can only be present in the right subarray
        else:
            return binarySearchRecursiveWithIdxGeeksForGeeks(list, mid + 1, end, num_to_find)
        
    # Element is not present
    else:
        return print("NOT FOUND", -1)

binarySearchRecursiveWithIdxGeeksForGeeks(list, 0, len(list) - 1, num_to_find)


print()
print("Binary Search While loop")

def binarySearchWhileLoop(list, x):
    begin = 0
    end = len(list) - 1
    while True:
        if begin > end:
            return print("NOT Found", -1)
        else:
            mid = begin + (end - begin) // 2
            if list[mid] == x:
                return print("Found at Idx: ", mid)
            elif x < list[mid]:
                end = mid - 1
            elif x > list[mid]:
                begin = mid + 1


binarySearchWhileLoop(list, num_to_find)    
