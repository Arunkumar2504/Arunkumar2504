
def swapNumber(a: list,  b: list) -> None:
    c = a[0]
    a[0] = b[0]
    b[0] = c
    return a, b