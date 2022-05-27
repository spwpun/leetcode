from typing import List

class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        """
        找到两个单词之间的最小距离
        """
        min_distance = 100000
        w1 = w2 = 0

        for i,word in enumerate(words):
            if word == word1:
                w1 = i
            if word == word2:
                w2 = i
            if w1 and w2:
                min_distance = min(abs(w1 - w2), min_distance)
        
        return min_distance

words = ["I","am","a","student","from","a","university","in","a","city"]
word1 = "a"
word2 = "student"
print(Solution().findClosest(words, word1, word2))
