import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)      # Shallow
c = copy.deepcopy(a)  # Deep

a[0][0] = 99
print(b)  # [[99, 2], [3, 4]] (affected)
print(c)
