def solution(S, B):
    # write your code in Python (Python 3.6)
    # S: str, '.' denotes the smoothe fragment of road, 'x' denotes the pothole
    # B: int, the budget to fix the road
    potholes = []
    cnt = 0
    for i in range(len(S)):
        if i >= 1 and S[i] == '.' and S[i - 1] == 'x':
            potholes.append(cnt)
            cnt = 0
            continue
        elif S[i] == '.':
            continue
        elif S[i] == 'x' and i == len(S) - 1:
            cnt += 1
            potholes.append(cnt)
        elif S[i] == 'x':
            cnt += 1
        else:
            print("Unknown Chracter!")
    # print(potholes)
    if len(potholes) == 0:
        return 0
    potholes.sort(reverse=True)
    current_budget = B
    max_fixed_holes = 0
    for i in range(len(potholes)):
        if potholes[i] >= current_budget:
            max_fixed_holes += current_budget - 1
            break
        else:
            max_fixed_holes += potholes[i]
            current_budget -= (potholes[i] + 1)
    print(max_fixed_holes)
    return max_fixed_holes
        


# Test
solution('...xxx..x....xxx.'*1000, 7000)