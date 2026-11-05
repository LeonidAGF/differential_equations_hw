from sympy import *
from IPython.display import display
from numpy import arange
import matplotlib.pyplot as plt

#2.1
x = symbols('x',positive = True)
y = Function('y')(x)
display(y)
y_ = Derivative(y, x)
display(y_)
de = Eq(y_,2*y*y*x*x)
display(de)
dsol_cyl = dsolve(de, y)
display(dsol_cyl)

C1 = Symbol('C1')
eq1 = dsol_cyl.subs({y:2,x:1})
sol1 = solveset(eq1, C1)
display(sol1)

dsol_cyl_f = dsol_cyl.subs(C1,tuple(sol1)[0])

display(eq1)
display(dsol_cyl_f)
print('\n')

#2.2
x = symbols('x',positive = True)
y = Function('y')(x)
display(y)
y_ = Derivative(y, x)
display(y_)
de = Eq((1/tan(x))*y_+y,2)
display(de)
dsol_cyl = dsolve(de, y)
display(dsol_cyl)

C1 = Symbol('C1')
eq1 = dsol_cyl.subs({y:0,x:pi/3})
sol1 = solveset(eq1, C1)
display(sol1)

dsol_cyl_f = dsol_cyl.subs(C1,tuple(sol1)[0])

display(eq1)
display(dsol_cyl_f)
print('\n')

#2.3
x = symbols('x',positive = True)
y = Function('y')(x)
display(y)
y_ = Derivative(y, x)
display(y_)
de = Eq(x*y_-2*y,0)
display(de)
dsol_cyl = dsolve(de, y)
display(dsol_cyl)

C1 = Symbol('C1')
eq1 = dsol_cyl.subs({y:1,x:1})
sol1 = solveset(eq1, C1)
display(sol1)

dsol_cyl_f = dsol_cyl.subs(C1,tuple(sol1)[0])

display(eq1)
display(dsol_cyl_f)
print('\n')

#2.4
a,x = symbols('a x',positive = True)
y = Function('y')(x)
display(y)
y_ = Derivative(y, x)
display(y_)
de = Eq(y_,1-a*x)
display(de)
dsol_cyl = dsolve(de, y)
display(dsol_cyl)

C1 = Symbol('C1')
eq1 = dsol_cyl.subs({y:0,x:2})
sol1 = solveset(eq1, C1)
display(sol1)

dsol_cyl_f = dsol_cyl.subs(C1,tuple(sol1)[0])

display(eq1)
display(dsol_cyl_f)
print('\n')