# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python (Python 3.6)
    cnt_filter = 0
    pollution_goal = sum(A) / 2
    A.sort(reverse=True)
    while True:
        print(A)
        cnt_filter += 1
        A[0] = A[0]/2
        if sum(A) <= pollution_goal:
            break
        A.sort(reverse=True)
    return cnt_filter

# Test
print(solution([5, 19, 8, 1]))