def MINAB(n):
    a1 = 0
    b1 = 0
    for a in range(1, n):
        for b in range(1, a):
            if n == a*b:
                a1 = a
                b1 = b
                break
    if len(str(a1)) >= len(str(b1)):
        return len(str(b1))
    elif len(str(a1)) < len(str(b1)):
        return len(str(a1))
print(MINAB(4))