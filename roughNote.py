def sumOrProduct(n, q):

    if q == 1:
        temp = 0
        return (n * (n + 1)//2)
    elif q == 2:
        temp = 1
        for i in range(1, n+1):
            temp = (i*temp) % (10**9 + 7)
        return temp

print(sumOrProduct(17, 2))
