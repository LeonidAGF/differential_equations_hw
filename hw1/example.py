from sympy import *
from IPython.display import display
from numpy import arange
import matplotlib.pyplot as plt

sigma, g, t, S = symbols('sigma g t S', positive=True)
display(sigma, g, t, S)
h = Function('h')(t)
display(h)
h_ = Derivative(h, t)
display(h_)
de = Eq(S * h_, -sigma * sqrt(2 * g * h))
display(de)
dsol_cyl = dsolve(de, h)
display(dsol_cyl)

C1 = Symbol('C1')

par = {g: 9.8, sigma: 0.1, S: 1.0, C1: 0.0}
p1 = plot(show=False)

# for c in range(-20,21,2):
#    par['C1'] = c
#    ds = dsol_cyl.rhs.subs(par)
#    p = plot(ds, (t,-120,120),show=False)
#    p1.extend(p)

# p1.show()

H = Symbol('H', positive=True)
eq1 = dsol_cyl.subs({h: H, t: 0})
display(eq1)
print('\n\n\n')

sol1 = solveset(eq1, C1)
display(sol1)

C2 = tuple(sol1)[1]
display(C2)

dsol_cyl_H = dsol_cyl.subs(C1, C2)
display(dsol_cyl_H)

eq2 = dsol_cyl_H.subs(h, 0)
sol2 = solveset(eq2, t)
display(sol2)

T1 = tuple(sol2)[0]
par = {g: 9.8, sigma: 0.1, S: 1.0, H: 0.0}
p2 = plot(show=False)

for ht in arange(1, 21, 1):
    par[H] = float(ht)
    ds = dsol_cyl_H.rhs.subs(par)
    t1 = float(T1.subs(par))
    p = plot(ds, (t, 0, t1), show=False)
    p2.extend(p)

p2.show()
