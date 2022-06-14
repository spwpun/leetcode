line = input()
min_cnt = []
for ch in line:
    tmp_cnt = line.count(ch)
    min_cnt.append((tmp_cnt, ch))
res = ""
min_cnt = sorted(min_cnt, key=lambda x: x[0])
m = min_cnt[0][0]
min_chs = []
for mi in min_cnt:
    if mi[0] == m and mi[0] not in min_chs:
        min_chs.append(mi[1])

for c in line:
    if c in min_chs:
        pass
    else:
        res += c
print(res)