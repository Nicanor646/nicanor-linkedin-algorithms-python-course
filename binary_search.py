import os
import random

def binary_search(data, target):
    low_pointer=0
    high_pointer=len(data)-1
    
    while low_pointer <= high_pointer:
        mid=(high_pointer+low_pointer)//2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low_pointer = mid + 1
        elif data[mid] > target:
            high_pointer = mid - 1
    return -1



array_len = int(os.environ.get("BINARY_SEARCH_ARRAY_LEN", 10))
max_val = int(os.environ.get("BINARY_SEARCH_MAX_VAL", 100))

data = [ random.randint(1,max_val) for idx in range(array_len) ]
data.sort()
print(f"Data: {data}")
target = int(input("Enter target value: "))
target_pos = binary_search(data, target)

if target_pos == -1:
    print("Target not found in data")
else:
    print(f"Target found in position: {target_pos}")

