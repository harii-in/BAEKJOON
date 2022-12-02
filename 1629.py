def DAC(A, B, C):
    if B == 1:
        return A % C
    elif B % 2 == 0:
        return (DAC(A, B//2, C) ** 2) % C
    else:
        return ((DAC(A, B//2, C) ** 2) * A) % C

A, B, C = map(int, input().split())
print(DAC(A, B, C))