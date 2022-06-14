import sys
import re

def check_passwd(passwd):
    if len(passwd) <= 8:
        return "NG"
    repeat = re.findall(r'(.{3,}).*\1', passwd) # \1 匹配第一个元组（）内容
    nums = re.findall(r'[0-9]', passwd)
    upper = re.findall(r'[A-Z]', passwd)
    lower = re.findall(r'[a-z]', passwd)
    other = re.findall(r'[^0-9A-Za-z]', passwd)
    if [nums, upper, lower, other].count([]) <=1 and repeat == []:
        return "OK"
    else:
        return "NG"

for line in sys.stdin:
    print(check_passwd(line[:-1]))