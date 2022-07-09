'''
排序法
兄弟单词：组成字符和长度一样，顺序不一样.

输入描述：
输入只有一行。 先输入字典中单词的个数n，再输入n个单词作为字典单词。 然后输入一个单词x 最后后输入一个整数k
输出描述：
第一行输出查找到x的兄弟单词的个数m 第二行输出查找到的按照字典顺序排序后的第k个兄弟单词，没有符合第k个的话则不用输出。
示例1
输入：
3 abc bca cab abc 1
输出：
2
bca
'''
list_ = input().split()
list_n = int(list_[0])
list_data = list_[1:-2]
word = list_[-2]
k = int(list_[-1])
bro_list = []
for w in list_data:
    l_w = list(w)
    l_w.sort()
    l_word = list(word)
    l_word.sort()
#     print(l_w, l_word)
    if l_w == l_word and w != word:
        bro_list.append(w)
print(len(bro_list))
if 0 <= k - 1 < len(bro_list):
    print(sorted(bro_list)[k-1])