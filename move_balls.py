'''
S: 
'''

def solution(S):
    # write your code in Python (Python 3.6)
    # S: str, only contains 'R' and 'W', 'R' denotes the red ball, 'W' denotes the white ball
    # we want to arrange all the red balls into a consistent segment. What is the minimum number of swaps needed to do that?
    if "R" not in S:
        return 0
    red_ball_index = []
    for i in range(len(S)):
        if S[i] == 'R':
            red_ball_index.append(i)
    # print(red_ball_index)
    # choose a middle position, others come to here
    if len(red_ball_index) == 1:
        return 0
    else:
        min_swap = 0
        mid = len(red_ball_index) // 2
        for i in range(len(red_ball_index)):
            diff = abs(red_ball_index[i] - red_ball_index[mid])
            if diff > 1:
                min_swap += diff - 1 - (abs(i - mid) - 1)
            
            if min_swap > 10**9:
                return -1
        return min_swap


# Test
print(solution("WRWRWRWR"))