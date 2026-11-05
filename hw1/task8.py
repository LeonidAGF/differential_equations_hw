from sympy import *
from IPython.display import display
from numpy import arange
import matplotlib.pyplot as plt

signa, g, t, r0,k = symbols('signa g t r0 k',positive = True)
display(signa, g, t, S)
h = Function('h')(t)
display(h)
h_ = Derivative(h, t)
display(h_)
de = Eq(pi*r0*r0*(h**(2*k))*h_,-signa*sqrt(2*g*h))
display(de)
dsol_cyl = dsolve(de, h)
display(dsol_cyl)

C1 = Symbol('C1')

par = {g:9.8, signa:0.1,k:10.0,C1:0.0,r0:1}
p1 = plot(show=False)

for c in range(-20,21,2):
    par['k'] = c
    ds = dsol_cyl.rhs.subs(par)
    p = plot(ds, (t,-120,120),show=False)
    p1.extend(p)

p1.show()

