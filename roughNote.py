def findDuplicate(arr: list) -> int:
   seen = set()
   for num in arr:
        if num in seen:
            return num
        seen.add(num)


arr = [3, 1, 3, 4, 2]
print(findDuplicate(arr))
