# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import random

def solution(X, Y):
    # write your code in Python (Python 3.6)
    # 求最大公因子
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    assert len(X) == len(Y)
    cnt = 0
    for i in range(len(X)):
        max_factor = gcd(X[i], Y[i])
        X[i] = X[i] // max_factor
        Y[i] = Y[i] // max_factor
    for i in range(len(X)):
        for j in range(i + 1, len(X)):
            if Y[i] == Y[j] and X[i] + X[j] == Y[i]:
                cnt += 1
    
    return cnt

# Test 
# Generate random data
N = 100000
X = [random.randint(1, 1000000000) for i in range(100000)]
Y = [random.randint(1, 1000000000) for i in range(100000)]
print(solution(X, Y))