def maxfun(n1,n2,n3):
    if n1 >= n2 and n1 >= n3 :
        print("n1 is biggest num")
        return n1
    elif n2 >= n1 and n2 >= n3 :
        print("n2 is biggest num")
        return n2
    else:
         print("n3 is biggest num")
         return n3
print(maxfun(597,1250,574))