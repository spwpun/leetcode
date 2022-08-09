class Solution:

    def __init__(self, capacity: int):
        # write code here
        self.datas = dict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        # write code here
        # 先删除，再添加
        ret = self.datas.get(key, -1)
        if key in self.datas.keys():
            self.datas.pop(key)
            self.datas[key] = ret
            return ret
        else:
            return -1

    def set(self, key: int, value: int) -> None:
        # write code here
        if self.capacity == len(self.datas):
            lru_key = next(iter(self.datas.keys()))
            self.datas.pop(lru_key)
        elif key in self.datas.keys():
            self.datas.pop(key)
        
        self.datas[key] = value
    
    def __repr__(self):
        return str(self.datas)

# Your LRUCache object will be instantiated and called as such:
solution = Solution(2)
solution.set(1, 1)
solution.set(2, 2)
print(solution.get(1))
solution.set(3, 3)
print(solution.get(2))