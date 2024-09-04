num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
if num1 > num2:
    small = num2
else:
    small = num1
for i in range (1 , small+1):
    if((num1 % i == 0) and (num2 % i == 0)):
        hcf = i
print(hcf)