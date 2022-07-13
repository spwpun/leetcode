'''
描述
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001

组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

数据范围：保证输入的是合法的 IP 序列
'''

def dot_2_oct(ip_dot_str):
    nums = ip_dot_str.split('.')
    bin_str = ''
    for num in nums:
        bin_str += bin(int(num))[2:].rjust(8, '0')
#     print("bin_str:",bin_str)
    return int(bin_str, 2)

def oct_2_dot(oct_num):
    bin_str = bin(oct_num)[2:].rjust(32, '0')
    dot_strs = []
    for i in range(0, 32, 8):
        num = int(bin_str[i:i + 8], 2)
        dot_strs.append(str(num))
    
    return '.'.join(dot_strs)

ip_dot_str = input()
num = int(input())