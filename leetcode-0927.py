'''
好久没练习，手好生！
判断两个字符串是否是变位词，即两个字符串中的字符种类和数量相同，但顺序不同。
'''

def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)