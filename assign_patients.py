'''
微软：分配病人
'''

def solution(A, B, S):
    # write your code in Python (Python 3.6)
    # A[]: preferences 1
    # B[]: preferences 2
    # S: total number of doctor slots
    if len(A) > S:
        return False
    if len(A) == 1:
        return True
    choices = []
    for i in range(len(A)):
        if A[i] > B[i]:
            choices.append((B[i], A[i]))
        else:
            choices.append((A[i], B[i]))
    choices.sort()
    # print(choices)
    ordered = []
    for i in range(len(choices)):
        if choices.count(choices[i]) >= 3:
            return False
        for prefer in choices[i]:
            if prefer not in ordered:
                ordered.append(prefer)
                break
    if len(ordered) == len(A):
        return True
    else:
        return False

# Test
print(solution([1,1,3,1,1], [2,5,4,3,4], 5))