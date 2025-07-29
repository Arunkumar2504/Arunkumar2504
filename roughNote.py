def twoSum(arr, target, n):
    # Write your code here.
    temp = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j]== target:
                return [arr[i],arr[j]]
    return [-1, -1]

print(twoSum([1, 2, 3, 4, 5], 9, 5))  # Example usage