'''Find the smallest number in an array'''

#Problem statement: Given an array, we have to find the smallest element in the array

#Intution: we can sort the array in ascending order, hence the smallest element will be at the 0th index.

def find_smallest_number(arr):
    arr.sort() #sorting the array in ascending order
    return arr[0] #return the element at index 0

my_array = [3,22,43,5,4,6,9]
result = find_smallest_number(my_array)
print(result)

print("\n")
'''A similar problem from leet code
2605. Form Smallest Number From Two Digit Arrays
Given two arrays of unique digits nums1 and nums2,
return the smallest number that contains at least one digit from each array. '''

class Solution(object):
    def minNumber(self, num1, num2):
        num1.sort() # Sort num1 in ascending order
        num2.sort() # Sort num2 in ascending order

        smallest1 = str(num1[0]) #smallest number in num1
        smallest2 = str(num2[0]) #smallest number in num2

        return smallest1 + smallest2 # concatinating the smallest numbers as a string

#input
num1 = [2, 5, 1, 3, 99]
num2 = [9, 4, 7, 6, 8]
solution = Solution()
result = solution.minNumber(num1, num2)
print(result)