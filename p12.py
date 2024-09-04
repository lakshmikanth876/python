#to check weather he year is leap year or not
year = float(input("enter the year:"))
if year%4==0 and year%100 != 0:
    print("the year is leap year")
    
else:
    print("this is not a leap year")