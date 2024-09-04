num = int(input("enter the number:"))
sum = 0 
if num < 0 :
    print("enetr the positive number")
else:
    print(num*((num+1)/2))
#or     
for i in range (1,num+1):
    sum += num
    num -= 1
print(sum)
    