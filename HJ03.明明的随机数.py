N = int(input())
randoms = []
for i in range(N):
    num = int(input())
    randoms.append(num)

randoms = sorted(list(set(randoms)))

for r in randoms:
    print(r)