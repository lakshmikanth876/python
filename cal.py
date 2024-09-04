num1 = float(input("enter the 1st number: "))
op = input("enetr the operator")
num2 = float(input("enter the 2nd number: "))
if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("invalid operator")