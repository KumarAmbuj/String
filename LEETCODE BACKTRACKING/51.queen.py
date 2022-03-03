class Solution:
    def placequeen(self, r, col, diag, rdiag, queens, n, res):
        if r == n:

            print('found')

            return
        
        for c in range(n):
            if  col[c] == False and diag[r + c] == False and rdiag[r - c + n - 1] == False:

                queens.append(c)
                col[c] = True
                diag[r + c] = True
                rdiag[r - c + n - 1] = True
                self.placequeen(r + 1, col, diag, rdiag, queens, n, res)
                queens.pop()
                col[c] = False
                diag[r + c] = False
                rdiag[r - c + n - 1] = False

    def solveNQueens(self, n: int):

        res = []

        queens = []


        col = [False for i in range(n)]
        diag = [False for i in range(2 * n - 1)]
        rdiag = [False for i in range(2 * n - 1)]

        self.placequeen(0, col, diag, rdiag, queens, n, res)
        return res

p=Solution()
res=p.solveNQueens(4)
print(res)
