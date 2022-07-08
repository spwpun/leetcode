'''
求最长回文字符串
Tag: dp
'''

def find_longest_palindrome(s, left, right):
    temp = 0
    # 由中心向两边扩展
    while left >= 0 and right < len(s) and s[left] == s[right]:
        temp = right - left + 1
        left -= 1
        right += 1
    
    return temp


line = input()
length = 0
for i in range(len(line)):
    length = max(length, find_longest_palindrome(line, i, i))
    length = max(length, find_longest_palindrome(line, i, i + 1))
print(length)