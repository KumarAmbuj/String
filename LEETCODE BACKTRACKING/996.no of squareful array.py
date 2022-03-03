import math


class Solution:

    def findNumber(self,i,hash,path,n):

        if i==n:
            self.count+=1
            return


        for x in hash:

            if hash[x]>0:

                if len(path)==0:
                    path.append(x)
                    hash[x]-=1

                    self.findNumber(i+1,hash,path,n)

                    hash[x]+=1
                    path.pop()

                elif len(path)>0:

                    z=path[-1]
                    sm=z+x

                    sr=math.sqrt(sm)

                    if sr==int(sr):

                        path.append(x)
                        hash[x]-=1
                        self.findNumber(i+1,hash,path,n)
                        hash[x]+=1
                        path.pop()




    def numSquarefulPerms(self, A):

        self.count = 0

        n = len(A)

        hash = {}

        for x in A:
            if x not in hash:
                hash[x] = 0
            hash[x] += 1

        path = []

        self.findNumber(0,hash,path,n)

        return self.count





A=[1,17,8]
p=Solution()
res=p.numSquarefulPerms( A)
print(res)

A=[2,2,2]
p=Solution()
res=p.numSquarefulPerms( A)
print(res)



