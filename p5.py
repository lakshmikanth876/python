import cmath #complex mah module 
a = 2
b =3 
c = 5
d = pow(b,2)-(4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print(sol1 , sol2)