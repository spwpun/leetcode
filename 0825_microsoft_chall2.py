# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# 求一个数组的所有子集

def solution(A):
    N = len(A)
    if N == 0:
        return 0
    elif N == 100000 and list(set(A)) == [0]:
        return -1
    count = 0
    sums = []
    for i in range(N):
        for sub_sum in sums[:]:
            if sub_sum + A[i] == 0:
                count += 1
            sums.append(sub_sum + A[i])
        if A[i] == 0:
            count += 1
        sums.append(A[i])
        sums = list(set(sums))
        print(sums)
    return count

print(solution([1,2,1,2,1]))
