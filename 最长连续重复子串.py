'''
求最长连续重复子串
'''

def longest_duplicate_substring(s):
    '''
    求最长连续重复子串
    '''
    if not s:
        return ''
    max_len = 1
    max_start = 0
    cur_len = 1
    cur_start = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
                max_start = cur_start
            cur_len = 1
            cur_start = i
    return s[max_start:max_start + max_len]
    

# Test , get 'bbbb'
s = 'abcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdbabcbbbbcdb'
print(longest_duplicate_substring(s))