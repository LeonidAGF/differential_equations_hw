from sympy import *
from IPython.display import display
from numpy import arange
import matplotlib.pyplot as plt

signa, g,h, r0,k = symbols('signa g h r0 k',positive = True)

t = Function('t')(h)

t_ = Derivative(t, h)

de = Eq(pi*r0*r0*(h**(2*k)),-signa*sqrt(2*g*h)*t_)
display(de)
dsol_cyl = dsolve(de, t)
display(dsol_cyl)

C1 = Symbol('C1')

par = {g:9.8, signa:0.1,k:10.0,C1:0.0,r0:1}
p1 = plot(show=False)

for c in range(-20,21,2):
    par['k'] = c
    ds = dsol_cyl.rhs.subs(par)
    p = plot(ds, (h,-120,120),show=False)
    p1.extend(p)

p1.show()

