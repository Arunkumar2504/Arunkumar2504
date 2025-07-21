
def findUnique(arr, n):
    # write your code here
    for i in range(len(arr)):
    
        if arr[i] == i+1:
            continue
        elif i not in arr:
            return i
    return n


print(findUnique([0, 0, 1, 2, 3, 5, 1, 2, 3, 4, 5], 6))  # Output: 6
