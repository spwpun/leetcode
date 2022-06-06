import math

def calc_prime_factors(n):
    '''
    计算质因子
    '''
    res = []
    while n % 2 == 0:
        res.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            res.append(i)
            n = n // i
    if n > 2:
        res.append(n)
    return res

n = int(input())
prime_factors = calc_prime_factors(n)
for p in prime_factors:
    print(p, end=' ')