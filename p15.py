#finding factorial of a number
fact = 1
num = int(input("enter the number:"))
if num < 0:
    num = -(num)
elif num == 0:
    print("factorial is one")
else:
    for i in range(1,num+1):
        fact = fact*i
print("the factorial of the number is:{}".format(fact))