#153 = 1^3+5^3+3^3 == 153 
num = int(input("enter the number:"))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit**3
    temp //= 10
if num == sum:
    print("it is an amstring number")
else:
    print("it is not an amstrong number")
