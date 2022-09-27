n, m = map(int, input().split())

def gcd(n, m):
    while m != 0:
        s = n % m
        n = m
        m = s
    return n

def lcm(n, m):
    s = (n*m) / gcd(n, m)
    return int(s)

print(gcd(n, m))
print(lcm(n, m))