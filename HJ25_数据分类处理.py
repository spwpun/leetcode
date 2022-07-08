'''
Tag：排序，模拟，字符串
'''

I_datas = input().split()[1:]
R_datas = map(int, input().split()[1:])

sorted_R_data = sorted(list(set(R_datas)))

res_data = []

for num in sorted_R_data:
    tmp_res = []
    cnt = 0
    for i in range(len(I_datas)):
        if str(num) in I_datas[i]:
            tmp_res.append(i)
            tmp_res.append(I_datas[i])
            cnt += 1
    if cnt != 0:
        res_data.append(num)
        res_data.append(cnt)
        res_data += tmp_res

print(len(res_data), end=" ")
for r in res_data:
    print(r, end=" ")