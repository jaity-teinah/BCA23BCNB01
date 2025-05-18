from sympy import *
x = symbols('x')
eqn = x**3 - x - 1
n=10
print("No. of stages: ",n)
a = 1
b = 2
for i in range(0,n):
    soll=(a+b)/2
    print(soll)
    sol2 = eqn.subs(x,soll)
    print(sol2)
    if sol2>0:
        b=soll
    if sol2<0:
        a=soll
print("The approximate real root is",soll)