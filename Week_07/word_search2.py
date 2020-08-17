# 单词搜索2
# https://leetcode-cn.com/problems/word-search-ii/
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        # 构建tria
        root = {}
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char,{})
            node["#"] = "#"
        # print(root)

        def dfs(board, i, j, str_in, node, res):
            k = board[i][j]
            str_in += k
            node = node[k]
            if '#' in node:
                res.add(str_in)
            tmp, board[i][j] = board[i][j], '@'
            for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                x, y = i+di, j+dj  
                if 0<=x<n and 0<=y<m and board[x][y]!='@'\
                 and board[x][y] in node:          
                    dfs(board, x, y, str_in, node, res)
            board[i][j] = tmp


        res = set()
        for i in range(n):
            for j in range(m):
                if board[i][j] in root:
                    dfs(board, i, j, '', root, res)
        return list(res)