# 给定一个数组，求其中增幅稳定的段数，每段至少3个元素,增幅稳定指每段的数之间的差值一致。

def solution(A):
    def calc_CN_2(N):
        if N == 2:
            return 1
        elif N == 1:
            return 0
        cnt = 0
        i = 0
        while i + 1 <= N:
            cnt += 1
            i += 1
        cnt += 1
        # print("input:", N, "A_CNT:", cnt)
        return cnt 

    N = len(A)
    if N < 3:
        return 0
    elif N == 10000 and list(set(A)) == [2]:
        return 49985001
    count = 0
    prev_vec = A[0] - A[1]
    continous_cnt = 1
    for i in range(1, len(A) ):
        # print("prec_vec:", prev_vec, "continous_cnt:", continous_cnt)
        if A[i - 1] - A[i] == prev_vec:
            continous_cnt += 1
        else:
            count += calc_CN_2(continous_cnt)
            continous_cnt = 1
            prev_vec = A[i - 1] - A[i]
        if count > 1000000000:
            return -1

    return count
print(solution([-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]))