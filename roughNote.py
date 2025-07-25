def missingAndRepeating(arr, n):

    n = len(arr)
    S = n * (n + 1) // 2
    S2 = n * (n + 1) * (2 * n + 1) // 6

    S_actual = sum(arr)
    S2_actual = sum(x * x for x in arr)

    diff1 = S_actual - S         # R - M
    diff2 = S2_actual - S2       # R^2 - M^2

    sum_R_M = diff2 // diff1     # R + M

    R = (diff1 + sum_R_M) // 2
    M = R - diff1

    return (M, R)


missingAndRepeating([5, 1, 2, 3, 4, 2], 6)