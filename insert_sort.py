'''
插入排序
'''

def insert_sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
        print(l)
    return l

def re():
    n = input()
    if '-' in n:
        tn = n[1:][::-1]
        print(tn)
    else:
        print(n[::-1])

insert_sort(l = [88,11,816,42,516,77])
re()