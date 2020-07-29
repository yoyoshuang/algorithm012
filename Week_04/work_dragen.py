# 单词接龙
# https://leetcode-cn.com/problems/word-ladder/
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        com_dict = {}
        
        for word in wordList:
            for i in range(len(word)):
                k = word[:i]+'*'+word[i+1:]
                if k not in com_dict:
                    com_dict[k] = []
                com_dict[k].append(word)
        # print(com_dict)
        queue = [(beginWord,1)]
        visited = {beginWord: True}

        while queue:
            current, level = queue.pop(0)
            
            for i in range(len(current)):
                inner_word = current[:i]+'*'+current[i+1:]
                if inner_word not in com_dict:
                    continue
                for word in com_dict[inner_word]:
                    if word == endWord:
                        return level+1
                    
                    if word in wordList and word not in visited:
                        queue.append((word, level+1))
                        visited[word] = True
        return 0

