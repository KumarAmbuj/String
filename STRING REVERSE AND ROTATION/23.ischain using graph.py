from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)


    def makegraph(self,arr):

        for i in range(len(arr)):
            for j in range(len(arr)):
                if i==j:
                    continue
                if arr[i][-1]==arr[j][0]:
                    self.addEdge(arr[i],arr[j])


    def dfs(self,u,s):
        s.add(u)
        for v in self.graph[u]:
            if v not in s:
                if self.dfs(v,s):
                    return True
            elif v in s:
                return True
        return False


    def isCycle(self,arr):

        s=set()
        for i in range(len(arr)):
            if arr[i] not in s:
                if self.dfs(arr[i],s):
                    return True

        return False

arr = ["geek", "king"]
g=Graph(len(arr))
g.makegraph(arr)
print(g.isCycle(arr))

arr = ["abc", "efg", "cde", "ghi", "ija"]
g=Graph(len(arr))
g.makegraph(arr)
print(g.isCycle(arr))
