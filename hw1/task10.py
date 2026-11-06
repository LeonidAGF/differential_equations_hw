from sympy import *
from IPython.display import display
from numpy import arange
import matplotlib.pyplot as plt

signa, g, t, r0,k = symbols('signa g t r0 k',positive = True)
display(signa, g, t)
h = Function('h')(t)
display(h)
h_ = Derivative(h, t)
display(h_)
de = Eq(pi*r0*r0*((10-h)**(2*k))*h_,-signa*sqrt(2*g*h))
display(de)
dsol_cyl = dsolve(de, h)
display(dsol_cyl)

C1 = Symbol('C1')

par = {g:9.8, signa:0.1,k:10.0,C1:10.0,r0:1}
p1 = plot(show=False)

for c in [-1, 0, 0.25, 0.5, 1, 2]:
    par[k] = c
    ds = dsol_cyl.rhs.subs(par)
    p = plot(ds, (t,0,120),show=False, label=f'k = {c}')
    p1.extend(p)

p1.legend = True
p1.xlabel='Время'
p1.ylabel='Высота'
p1.show()
