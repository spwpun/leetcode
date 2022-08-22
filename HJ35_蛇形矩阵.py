'''
观察i、j的变化规律， 数组操作
描述
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。

例如，当输入5时，应该输出的三角形为：

1 3 6 10 15

2 5 9 14

4 8 13

7 12

11

输入描述：
输入正整数N（N不大于100）

输出描述：
输出一个N行的蛇形矩阵。

示例1
输入：
4
复制
输出：
1 3 6 10
2 5 9
4 8
7
'''
N = int(input())
i = 0
j = 0
prev_i = i
A = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
n = 1
while j != N:
#     print(i, j)
    if j == N - 1:
        A[i][j] = n
        break
    A[i][j] = n
    n += 1
    if i == 0:
        i = prev_i + 1
        j = 0
    elif j == 0:
        prev_i = i
        i = i - 1
        j = j + 1
    else:
        i = i - 1
        j = j + 1
for i in range(N):
    for j in range(N):
        if A[i][j] != 0:
            if j == N - 1 or A[i][j + 1] == 0:
                print(A[i][j])
            else:
                print(A[i][j], end=' ')
    