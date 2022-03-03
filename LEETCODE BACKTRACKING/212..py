class Solution:
    def findword(self, nc, i, j, board, word, m, n, vis):
        if nc == len(word):
            print(word)
            return True

        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]

        for k in range(4):
            x = i + di[k]
            y = j + dj[k]

            if x >= 0 and x < m and y >= 0 and y < n and vis[x][y] == False and board[x][y] == word[nc]:

                vis[x][y] = True
                if self.findword(nc + 1, x, y, board, word, m, n, vis):
                    return True
                vis[x][y]=False

        return False

    def findWords(self, board, words):
        res = []
        m = len(board)
        n = len(board[0])

        for word in words:



            vis = [[False for j in range(n)] for i in range(m)]

            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        vis[i][j] = True
                        if self.findword(1, i, j, board, word, m, n, vis):
                            res.append(word)
                        vis[i][j] = False

        return res
board=[["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words=["oa","oaa"]
p=Solution()
res=p.findWords( board, words)
print(res)

