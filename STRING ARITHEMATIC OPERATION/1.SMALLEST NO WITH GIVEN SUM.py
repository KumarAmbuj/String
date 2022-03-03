def findsmallestno(n):
    m=n
    res=''

    for i in range(9,0,-1):
        k=n//i
        res=str(i)*k+res
        n=n%i

        if n==0:
            break

    res=res+'0'*m
    return res

print(findsmallestno(24))