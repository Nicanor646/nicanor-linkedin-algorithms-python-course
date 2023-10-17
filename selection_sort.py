import os

def find_min(array):
    min_index = 0
    for idx in range(len(array)):
        if array[idx] < array[min_index]:
            min_index = idx
    return array[min_index], min_index

def selection_sort(array):
    for idx in range(len(array)):
        tmp_value = array[idx]
        min_value, min_index = find_min(array[idx:])
        array[idx] = min_value
        array[min_index+idx] = tmp_value
    return array

test_array = [4, 17, 6, 8, 9, 3, 14]
print(f"The sorted array is: {selection_sort(test_array)}")
print(all(test_array[idx-1] <= test_array[idx] for idx in range(1,len(test_array))))