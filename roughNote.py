def findDuplicate(arr: list) -> int:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                value = arr[i]
                return value


arr = [3, 1, 3, 4, 2]
print(findDuplicate(arr))

# --------------------------------------------------------------------------------