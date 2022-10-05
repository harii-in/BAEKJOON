T = int(input())
for _ in range(T):
    A, B = map(str, input().split())

    x = sorted(list(A))
    y = sorted(list(B))

    if x == y:
        print("%s & %s are anagrams. " %(A, B))
    else:
        print("%s & %s are NOT anagrams. " %(A, B))