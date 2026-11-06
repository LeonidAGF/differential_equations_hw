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

par = {g:9.8, signa:0.1,k:10.0,C1:10000.0,r0:1}
p1 = plot(show=False)

for c in [0, 0.25, 0.5, 1, 2]:
    par[k] = c
    ds = dsol_cyl.rhs.subs(par)
    p = plot(ds, (h,0,12),show=False, label=f'k = {c}')
    p1.extend(p)

p1.legend = True
p1.xlabel='Высота'
p1.ylabel='Время'
p1.show()

