# Test meituan 1

n,t = map(int, input().split())
orders = list(map(int, input().split()))
# assert n == len(orders)
orders.sort()
magic_cnt = 0
ordinary_cnt = 1
for i in range(n):
    if ordinary_cnt*t <= orders[i]:
        ordinary_cnt += 1
    else:
        magic_cnt += 1
print(magic_cnt)

# Test 2
# def cnt_infloor(floor):
#     remain_cnt = 0
#     for dd in floor:
#         remain_cnt += dd.count(0)
    
#     return remain_cnt


# n, m, k = map(int, input().split())
# floor = [[0 for i in range(n)] for j in range(m)]
# instructions = input()
# i, j = 0, 0
# floor[i][j] = 1
# step_cnt = 0
# # remain_cnt = n*m - 1
# for instr in instructions:
#     if instr == 'A':
#         j -= 1
#         floor[i][j] = 1
#     elif instr == 'W':
#         i -= 1
#         floor[i][j] = 1
#     elif instr == 'S':
#         i += 1
#         floor[i][j] = 1
#     elif instr == 'D':
#         j += 1
#         floor[i][j] = 1
#     step_cnt += 1
#     remain_cnt = cnt_infloor(floor)
#     if remain_cnt == 0:
#         break
# if remain_cnt == 0:
#     print("Yes")
#     print(step_cnt)
# else:
#     print("No")
#     print(remain_cnt)

# Test 3

# n = int(input())
# nums = list(map(int, input().split()))

# third_tuples = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             if nums[i] - nums[j] == 2*nums[j] - nums[k]:
#                 third_tuples += 1
# print(third_tuples)

# 特工编号


class agent():
    def __init__(self, id, up_id, down_ids):
        self.id = id
        self.up_id = up_id
        self.down_ids = down_ids  # list

    def find_in_down_ids(self, id):
        if id in self.down_ids:
            return True


num_agents, request_cnt = map(int, input().split())
print(num_agents, request_cnt)
agents = [agent(id = i + 1, up_id = -1, down_ids = []) for i in range(num_agents)]
up_ids = list(map(int, input().split()))
for idx, value in enumerate(up_ids):
    agents[idx + 1].up_id = value
    agents[value - 1].down_ids.append(idx + 2)
for i in range(request_cnt):
    cur_id, target_id = map(int, input().split())
    print(cur_id, end=' ')
    if cur_id == target_id:
        print("\n")
        continue
    cur_agent = agents[cur_id - 1]
    while True:
        if target_id in cur_agent.down_ids:
            print(target_id, end='\n')
            break
        else:
            cur_agent = agents[cur_agent.up_id - 1]
            print(cur_agent.id, end=' ')
# Test


