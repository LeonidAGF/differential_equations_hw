print(((300000000)**2)/(2*9.8)) #высота столба воды такого, чтобы вода вытекала со скростью света

from sympy import *
from IPython.display import display
from numpy import arange
import matplotlib.pyplot as plt

signa, g, t, r0,c = symbols('signa g t r0 c',positive = True)
display(signa, g, t)
h = Function('h')(t)
display(h)
h_ = Derivative(h, t)
display(h_)
de = Eq(c,signa*sqrt(2*g*h)/(pi*r0*r0*(h**(2))))
display(de)
dsol_cyl = solve(de, h)[0]
display(dsol_cyl)

par = {g: 9.8, signa: 1, r0: 10, c: 300000000}
res = dsol_cyl.subs(par)

print("высота" ,res)
