from sympy import *
from IPython.display import display
from numpy import arange
import matplotlib.pyplot as plt

signa, g, h, r0, k = symbols('signa g h r0 k', positive=True)

t = Function('t')(h)
t_ = Derivative(t, h)

de = Eq(pi*r0*r0*(h**(2*k)), -signa*sqrt(2*g*h)*t_)
display(de)
dsol_cyl = dsolve(de, t)
display(dsol_cyl)

C1 = Symbol('C1')

H = Symbol('H', positive=True)
eq1 = dsol_cyl.subs({h: H, t: 0})
display(eq1)

sol1 = solveset(eq1, C1)
display(sol1)

C2 = tuple(sol1)[0]
display(C2)

dsol_cyl_H = dsol_cyl.subs(C1, C2)
display(dsol_cyl_H)

T1 = dsol_cyl_H.rhs
display(T1)

par = {g: 9.8, signa: 0.1, k: 1, r0: 1,H:10}
p2 = plot(show=False)

for kt in [0.5, 1, 2]:
    par[k] = kt
    ds = dsol_cyl_H.rhs.subs(par)
    t1 = float(ds.subs(h, 0))
    p = plot(ds, (h, 1, par[H]), show=False)
    p2.extend(p)

#p2.legend = True
p2.xlabel = 'Высота'
p2.ylabel = 'Время'
p2.show()