import math

def isPrime(num):
    '''
    判断一个数是否是素数
    '''
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
    
def find(odd, matcheven, evens, v):
    """
    判断奇数是否能找到伴侣
    """
    for i in range(len(evens)):
        if isPrime(odd + evens[i]) and v[i] == 0:
            v[i] = 1
            if matcheven[i] == -1 or find(matcheven[i], matcheven, evens, v):
                matcheven[i] = odd
#                 print(matcheven, odd)
                return True
    return False

n = int(input())
nums = map(int, input().split())
odds = []
evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
matcheven_r = [-1 for _ in range(len(evens))]
cnt = 0
for j in range(len(odds)):
    v = [0 for _ in range(len(evens))]
    if find(odds[j], matcheven_r, evens, v):
        cnt += 1
# print(odds, evens, matcheven_r)
print(cnt)