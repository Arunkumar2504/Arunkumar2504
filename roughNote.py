arr = [1, 2, 3, 4, 1, 6]
value = 0
for i in arr:
    value = arr[i + 1]
    if arr[i] == value:
        print(arr[i])
