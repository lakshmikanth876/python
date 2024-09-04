def recur(n):
    if n<=1:
        return n
    else:
        return(recur(n-1) + recur(n-2))
nterms = 10
if nterms <= 0:
    print("enter a positive number")
else:
    for i in range(nterms):
        print(recur(i))