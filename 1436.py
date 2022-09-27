N = int(input())
cnt = 0
first = 666

while True:
    if '666' in str(first):
        cnt += 1
    if cnt == N:
        print(first)
        break
    first += 1