def rotateArray(arr: list, k: int) -> list:
    k = k % len(arr)
    return arr[k:] + arr[:k]


print(rotateArray([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]