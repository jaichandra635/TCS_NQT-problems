# Find the largest element in an array
'''
Given an array, we have to find the largest element in the array
'''

# Intution: sorting array in ascending order, and hence largest element will be last index element

''' Approach: 1. Sort the array in ascending order
              2. Print the (sixe of the array -1)th index.'''
''' DryRun: 
before sorting: arr[] = [8, 4, 3, 2,1 ]
after sorting: arr[] = [1,2,3,4,8]
answer: return arr[sizeofthearray - 1] = 5 '''

def find_largest_element(arr):
    arr.sort()
    return arr[-1]

my_array = [45, 22, 53, 21, 566, 332, 553, 523, 98]
result = find_largest_element(my_array)
print(result)