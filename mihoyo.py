'''
满足：除了叶子节点，所有节点的邻点一点过存在两种和它本身不同的颜色。

输入描述：
第一行输入一个正整数n, 代表节点的数量
接下来的n-1行, 每行输入两个正整数u, v, 代表节点u和v有一条无向边相连
2 <= n <= 10^5

输出描述：
一个长度为n的，仅包含'R', 'G', 'B'三种字符的字符串，代表节点的颜色，分别是红色，绿色，蓝色。
有多解时输出任意解法即可。
'''
tree = []

class mynode():
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.color = ''
    
    def add_edge(self, another_node_index):
        self.edges.append(another_node_index)
    
    def check_for_leaf_node(self):
        assert len(self.edges) >= 1
        if len(self.edges) == 1:
            return True
        else:
            return False
    
    def set_color(self, color):
        self.color = color
    
    def check_color_right(self):
        cnt = 0
        for edge in self.edges:
            if self.color != tree[edge].color:
                cnt += 1
        if cnt >= 2:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return "index:" + str(self.index + 1) + "\nedges:" + str(self.edges) + "\ncolor:" + self.color

def main():
    global tree
    N = int(input())
    colors_1 = 'GB'
    colors_2 = 'RB'
    colors_3 = 'RG'
    tree = [None for i in range(N)]
    for i in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if tree[u] == None:
            tree[u] = mynode(u)
        if tree[v] == None:
            tree[v] = mynode(v)
        tree[u].add_edge(v)
        tree[v].add_edge(u)
    for node in tree:
        if node.check_for_leaf_node():
            continue
        if node.color == '':
            node.set_color('R')
        if node.color == 'R':
            for i in range(2):
                tree[node.edges[i]].set_color(colors_1[i])
        elif node.color == 'G':
            for i in range(2):
                tree[node.edges[i]].set_color(colors_2[i])
        elif node.color == 'B':
            for i in range(2):
                tree[node.edges[i]].set_color(colors_3[i])
    ans = ''
    for node in tree:
        if node.check_color_right():
            ans += node.color
        else:
            ans += 'R'
    print(ans)
    return ans
            

if __name__ == "__main__":
    main()