class Node:
    def __init__(self,c,f):
        self.c=c
        self.f=f
def Maxheap():
    heap=[]
    return heap
def Add(heap,arr):
    for x in arr:
        heap.append(x)
    Buildmaxheap(heap)

def Maxheapify(heap,i,n):
    min=i
    l=2*i+1
    r=2*i+2

    if l<n and heap[l].f>heap[i].f:
        min=l
    if r<n and heap[r].f>heap[min].f:
        min=r

    if min!=i:
        heap[i],heap[min]=heap[min],heap[i]
        Maxheapify(heap,min,n)

def Buildmaxheap(heap):
    n=len(heap)

    for i in range((n-1)//2,-1,-1):
        Maxheapify(heap,i,n)

def Extractmax(heap):
    n=len(heap)
    a=heap[0]
    heap[0]=heap[n-1]
    heap.pop()
    n=len(heap)
    Maxheapify(heap,0,n)
    return a
def Insert(heap,x):
    heap.append(x)
    i=len(heap)-1

    while(i>0 and heap[i].f>heap[i//2].f):
        heap[i],heap[i//2]=heap[i//2],heap[i]
        i=i//2
def Size(heap):
    return len(heap)


def findSumOfSquare(s,k):
    dic={}
    for x in s:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    arr=[]

    for x in dic:
        arr.append(Node(x,dic[x]))

    heap=Maxheap()
    Add(heap,arr)

    while(k>0):
        x=Extractmax(heap)

        if k<=x.f:
            x.f=x.f-k
            k=0
            Insert(heap,x)
        elif k>x.f:
            k=k-x.f
            x.f=0
            Insert(heap,x)

        if k==0:
            break


    res=0
    while(Size(heap)>0):
        x=Extractmax(heap)

        res=res+(x.f*x.f)
    return res



s = 'abccc'
K = 2

print(findSumOfSquare(s,K))


s = 'aaabbbbbccccc'
K = 1

print(findSumOfSquare(s,K))






