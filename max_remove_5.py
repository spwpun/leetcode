# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python (Python 3.6)
    s = list(str(N))
    if s.count('5') == 1:
        s.remove('5')
        return int(''.join(s))
    else:
        if '-' in s:
            s = s[1:][::-1]
            s.remove('5') 
            s = s[::-1]
            return int('-'+''.join(s))
        else:
            s.remove('5')
            return int(''.join(s))

print(solution(-5859))