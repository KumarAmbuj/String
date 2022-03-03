from collections import defaultdict

def Stack():
    stack=[]
    return stack
def isEmpty(s):
    return len(s)==0
def Push(s,x):
    s.append(x)
def Pop(s):
    return s.pop()
def Size(s):
    return len(s)

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def makegraph(self,arr):
        for k in range(len(arr)-1):
            word1=arr[k]
            word2=arr[k+1]

            i=0
            j=0
            while(word1[i]==word2[j]):
                i+=1
                j+=1
            self.addEdge(word1[i],word2[j])
    def dfs(self,u,s,hash):
        hash.add(u)
        for v in self.graph[u]:
            if v not in hash:
                self.dfs(v,s,hash)
        Push(s,u)
    def topological(self):
        s=Stack()
        arr=['a','b','c','d']
        hash=set()
        for i in range(len(arr)):
            if arr[i] not in hash:
                self.dfs(arr[i],s,hash)
        while(Size(s)>0):
            print(Pop(s))

arr=["baa", "abcd", "abca", "cab", "cad"]
g=Graph(4)
g.makegraph(arr)
g.topological()

