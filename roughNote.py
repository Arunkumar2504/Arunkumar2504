def largestElement(arr: [], n: int) -> int:
    temp = 0
    for i in range(n):
        if arr[i] > temp:
            temp = arr[i]
    return temp


print(largestElement([1, 2, 5, 4, 6, 2], 5))
