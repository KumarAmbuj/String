def isvalid(board,row,col,word,n1,n,ROW,COL,vis):
    if row>=0 and row<ROW and col>=0 and col<COL and board[row][col]==word[n1] and vis[row][col]==False:
        return True
    return False

def findallpath(board,row,col,path,n1,n,ROW,COL,vis,word):
    if n1==n:
        print(path)
        return
    if n1>n:
        return

    rowNum = [-1, -1, -1, 0, 0, 1, 1, 1]
    colNum = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(8):
        x=row+rowNum[i]
        y=col+colNum[i]

        if isvalid(board,x,y,word,n1,n,ROW,COL,vis):
            vis[x][y] = True
            res=path+word[n1]+'('+str(x)+','+str(y)+')'
            findallpath(board,x,y,res,n1+1,n,ROW,COL,vis,word)
            vis[x][y]=False







def findpath(board,ROW,COL,word):
    vis=[[False for i in range(COL)]for  j in range(ROW)]
    n=len(word)

    for i in range(ROW):
        for j in range(COL):
            if board[i][j]==word[0]:
                vis[i][j]=True
                path=word[0]+'('+str(i)+','+str(j)+')'
                findallpath(board,i,j,path,1,n,ROW,COL,vis,word)



mat = [['B', 'N', 'E', 'Y', 'S'],
        ['H', 'E', 'D', 'E', 'S'],
        ['S', 'G', 'N', 'D', 'E']]
word = list("DES")

findpath(mat,3,5,word)


mat = [['B', 'N', 'E', 'Y', 'S'],
        ['H', 'E', 'D', 'E', 'S'],
        ['S', 'G', 'N', 'D', 'E']]
char =list('DEN')

findpath(mat,3,5,char)