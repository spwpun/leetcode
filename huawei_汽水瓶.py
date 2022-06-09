def explore(n):
    '''
    计算最多喝到汽水
    '''
    cnt = 0
    if n == 2 or n == 3:
        return 1
    elif n == 1:
        return 0
    else:
        tmp = 0
        if n <= 3:
            tmp = explore(n)
        else:
            tmp = n // 3
            tmp += explore(tmp + (n%3))
        cnt += tmp
    return cnt

while True:
    n = int(input())
    if n == 0:
        break
    cnt = explore(n)
    print(cnt)