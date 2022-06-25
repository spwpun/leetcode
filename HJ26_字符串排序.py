'''
Tag：插入排序应用到字符串中
'''
line = list(input())
for i in range(1, len(line)):
    if not line[i].isalpha():
        continue
    swap_index = i
    for j in range(i, -1, -1):
        if line[j].isalpha() and line[j].lower() > line[swap_index].lower():
            line[swap_index], line[j] = line[j], line[swap_index]
            swap_index = j
            
print(''.join(line))