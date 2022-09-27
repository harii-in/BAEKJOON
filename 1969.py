N, M = map(int, input().split())
DNA = [list(map(str, input().strip())) for _ in range(N)]

tmp = ""
cnt = 0

for i in range(M):
    DNAs = {"A" : 0, "T" : 0, "G" : 0, "C" : 0}

    for j in range(N):
        DNAs[DNA[j][i]] += 1

    if max(DNAs["A"], DNAs["T"], DNAs["G"], DNAs["C"]) == DNAs["A"]:
        tmp += "A" # DNA
        cnt += DNAs["T"] + DNAs["G"] + DNAs["C"]
    elif max(DNAs["A"], DNAs["T"], DNAs["G"], DNAs["C"]) == DNAs["C"]:
        tmp += "C"
        cnt += DNAs["A"] + DNAs["T"] + DNAs["G"]

    elif max(DNAs["A"], DNAs["T"], DNAs["G"], DNAs["C"]) == DNAs["G"]:
        tmp += "G"
        cnt += DNAs["A"] + DNAs["T"] + DNAs["C"]

    elif max(DNAs["A"], DNAs["T"], DNAs["G"], DNAs["C"]) == DNAs["T"]:
        tmp += "T"
        cnt += DNAs["A"] + DNAs["G"] + DNAs["C"]

print(tmp)
print(cnt)