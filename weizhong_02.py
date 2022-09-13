def solution(a, b):
    cnt = 0
    if a > b:
        while a > b:
            a = a >> 1
            cnt += 1
    elif a < b:
        while a < b:
            a = a << 1
            cnt += 1
    if a == b:
        # print(cnt)
        c1 = cnt//3
        c2 = (cnt%3)//2
        c3 = (cnt%3)%2
        # print(c1, c2, c3)
        return c1+c2+c3
    else:
        return -1
    


n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(solution(a,b))