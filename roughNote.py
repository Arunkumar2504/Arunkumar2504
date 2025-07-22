
def findUnique(arr, n):
    # write your code here
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                break
            continue

    return i


print(findUnique([0, 0, 1, 2, 3, 5, 1, 2, 3, 4, 5], 6))
