####################################################
## The Actual Memory Size of Your USB Flash Drive ##
####################################################

# Create a function that takes the memory size (ms) as an argument and returns the actual memory size. 
#
# Examples:
# 
# actualMemorySize("32GB")
# output = "29.76GB"
# 
# actualMemorySize("2GB")
# output = "1.86GB"
# 
# actualMemorySize("512MB")
# output = 476MB
# 
# Notes
# - The actual storage loss on a USB devise is 7% of the overall memory size
# - If the actual memory size was greater than 1 GB, round your result to two decimal places
# - If the memory size after adjustment is smaller than 1GB, return the result in MB
# - For the purposes of this challenge, there are 1000 MB in a Gigabyte

def actualMemorySize(ms):
    memory = int(ms[:len(ms) - 2])
    unit_measure = ms[len(ms) - 2:]
    # Compute the actual storage
    actual_memory = memory - (memory * 0.07)    
    if unit_measure == "GB":
        # Check if actual memory is still in GB. Otherwise convert the result to megabyte
        if actual_memory < 1:
            actual_memory = round(actual_memory * 1000)
            return f'{actual_memory}MB'
        else:
            actual_memory = round(actual_memory, 2)  
            return f'{actual_memory}{unit_measure}'
    else:
        actual_memory = round(actual_memory)
        return f'{actual_memory}{unit_measure}'


print(actualMemorySize("32GB"))
print(actualMemorySize("2GB"))
print(actualMemorySize("512MB"))
print(actualMemorySize("1GB"))