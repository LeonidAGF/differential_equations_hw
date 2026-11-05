from sympy import *
from IPython.display import display
from numpy import arange
import matplotlib.pyplot as plt

#1.1
x = symbols('x',positive = True)
y = Function('y')(x)
display(y)
y_ = Derivative(y, x)
display(y_)
de = Eq(y_,y*y)
display(de)
dsol_cyl = dsolve(de, y)
display(dsol_cyl)
print('\n')

#1.2
x = symbols('x',positive = True)
y = Function('y')(x)
display(y)
y_ = Derivative(y, x)
display(y_)
de = Eq(ln(x)*x*y_,y)
display(de)
dsol_cyl = dsolve(de, y)
display(dsol_cyl)
print('\n')

#1.3
x = symbols('x',positive = True)
y = Function('y')(x)
display(y)
y_ = Derivative(y, x)
display(y_)
de = Eq(x*y+(x+1)*y_,0)
display(de)
dsol_cyl = dsolve(de, y)
display(dsol_cyl)
print('\n')

#1.4
x = symbols('x',positive = True)
y = Function('y')(x)
display(y)
y_ = Derivative(y, x)
display(y_)
de = Eq(y_+1,x*y*y+x-y*y)
display(de)
dsol_cyl = dsolve(de, y)
display(dsol_cyl)
print('\n')