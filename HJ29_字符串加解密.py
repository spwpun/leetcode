'''
描述
对输入的字符串进行加解密，并输出。

加密方法为：

当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；

当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；

其他字符不做变化。

解密方法为加密的逆过程。
数据范围：输入的两个字符串长度满足 1 \le n \le 1000 \1≤n≤1000  ，保证输入的字符串都是只由大小写字母或者数字组成
输入描述：
第一行输入一串要加密的密码
第二行输入一串加过密的密码

输出描述：
第一行输出加密后的字符
第二行输出解密后的字符

输入：
abcdefg
BCDEFGH
输出：
BCDEFGH
abcdefg
'''

line = input()
cipher = input()
output = ""
plain = ""
# encrypt
for i in range(len(line)):
    if line[i].islower():
        tn = ord(line[i].upper()) + 1
        if tn == ord("Z") + 1:
            tn = ord("A")
        output += chr(tn)
    elif line[i].isupper():
        tn = ord(line[i].lower()) + 1
        if tn == ord("z") + 1:
            tn = ord("a")
        output += chr(tn)
    elif line[i].isdigit():
        output += str((int(line[i]) + 1)%10)
    else:
        output += line[i]
# decrypt
for i in range(len(cipher)):
    if cipher[i].islower():
        tn = ord(cipher[i].upper()) - 1
        if tn == ord("A") - 1:
            tn = ord("Z")
        plain += chr(tn)
    elif cipher[i].isupper():
        tn = ord(cipher[i].lower()) - 1
        if tn == ord("a") - 1:
            tn = ord("z")
        plain += chr(tn)
    elif cipher[i].isdigit():
        tn = int(cipher[i]) - 1
        if tn == -1:
            tn = 9
        plain += str(tn)
    else:
        plain += cipher[i]
print(output, plain, sep="\n")