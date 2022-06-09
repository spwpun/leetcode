'''
背包问题，求购物单最大满意度
N: 最大耗费
m：商品数量
v：商品价格
p: 商品重要度
q: 主件与否，0为主件，其余为附件，q为其主件编号，从1开始,最多两个附件
'''

line = input()
N,m = map(int,line.split())
v = [0]*m
p = [0]*m
q = [0]*m
dp = [0]*(N+1)
# 分组背包
wt = [[] for _ in range(m)]
val = [[] for _ in range(m)]

for i in range(m):
    line = input()
    v[i],p[i],q[i] = map(int,line.split())
    if q[i] == 0: #主件
        wt[i].append(v[i]) # 价格
        val[i].append(v[i]*p[i]) # 满意度
print("wt:",wt, "val:",val)
for i in range(m):
    if q[i] != 0: #附件
        primary_idx = q[i] - 1
        l = len(wt[primary_idx]) # 主件的商品数量
        print("主件商品数量：",l, "主件编号：",primary_idx+1)
        wt[primary_idx].append(wt[primary_idx][0] + v[i]) # 购买该附件时的价格（加上主件）
        val[primary_idx].append(val[primary_idx][0] + v[i]*p[i]) # 购买该附件时的满意度（加上主件）
        if l == 2: # 2个附件
            wt[primary_idx].append(wt[primary_idx][1] + v[i]) # 购买该附件时的价格（加上主件）
            val[primary_idx].append(val[primary_idx][1] + v[i]*p[i]) # 购买该附件时的满意度（加上主件）
    
    print("wt:",wt, "val:",val)

for i in range(m):
    if not wt[i]:
        continue
    for w in range(N, -1, -1):
        for j in range(len(wt[i])):
            if w >= wt[i][j]: #价格大于等于购买该商品及其j+1个附件的价格
                dp[w] = max(dp[w], dp[w-wt[i][j]] + val[i][j]) # 计算满意度
    print("dp:",dp)
print(dp[N])


