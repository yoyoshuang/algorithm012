# 单词接龙
# https://leetcode-cn.com/problems/word-ladder/submissions/
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
       
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        begins = {beginWord}
        backs = {endWord}
        res = 1
        
        while begins:
            res += 1
            next_begins = set()
            for word in begins:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        new_word =  word[:i]+c+word[i+1:]
                        if new_word in backs:
                            return res
                        if new_word in wordList:
                            next_begins.add(new_word)
                            wordList.remove(new_word)
            begins = next_begins
            if len(begins)>len(backs):
                begins, backs = backs, begins
        return 0
