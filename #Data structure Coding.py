#  Data structure Coding

import array


Array = array.array('i', [10, 20, 30, 40, 50])
# Accessing elements
print(Array[0])

# Displaying all elements
for i in range(len(Array)):
    print(Array[i])

# # Adding elements and displaying
Array.append(60)
for i in range(len(Array)):
    print(Array[i])

# # Searching for a number and index in the array
i = 0
Finding_number = int(input("Please enter the number you want to find: "))
for i in range(len(Array)):
    if Array[i] == Finding_number:
        print(f"Yes, the number is present in {i} index in the array.")
        i += 1
        break
    elif Array[i] != Finding_number:
        print(f"Your Number is not in {i} index")

# Problem statement
# You are given an array ‘arr’ containing ‘n’ integers. You are also given an integer ‘num’, and your task is to find whether ‘num’ is present in the array or not .


# If ‘num’ is present in the array, return the 0-based index of the first occurrence of ‘num’. Else, return -1.


# Example:
# Input: ‘n’ = 5, ‘num’ = 4
# 'arr' = [6, 7, 8, 4, 1]

# Output: 3

# Explanation:
# 4 is present at the 3rd index.
# Detailed explanation(Input/output format, Notes, Images)
# Sample Input 1:
# 5 4
# 6 7 8 4 1
# Sample Output 1:
# 3
# Explanation Of Sample Input 1:
# 4 is present at the 3rd index.
def linearSearch(n: int, num: int, arr: [int]) -> int:  # type: ignore
    # Write your code here.
    Index_value = arr.index(num)
    print(Index_value)
    pass


n = int(input("Please enter the number of elements in the array: "))
num = int(input("Please enter the number you want to find: "))
arr = list(map(int, input("Please enter the lists: ").split()))

linearSearch(n=n, num=num, arr=arr)

# Problem statement
# Given an array of size N, find the sum of its elements.


n = int(input())
N = list(map(int, input().split()))
total = sum(N)
print(total)


# Function to find the largest element
def largestElement(arr, n):
    max_element = arr[0]  # Assume the first element is the largest

    for i in range(1, n):
        if arr[i] > max_element:
            max_element = arr[i]

    return max_element


# ---- Main code ----
# Take input
n = int(input())                       # First line: number of elements
arr = list(map(int, input().split()))  # Second line: space-separated elements

# Call the function and print the result
print(largestElement(arr, n))
