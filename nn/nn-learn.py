from micrograd.engine import Value

"""
a -
    * - e -
b -         + - d -
        c -         * - L
                f -
"""
a = Value(2.0, label='a')
b = Value(-3.0, label='b')
c = Value(10.0, label='c')
e = a*b; e.label = 'e'
d = e + c; d.label = 'd'
f = Value(-2.0, label='f')
L = d * f; L.label = 'L'

# Manual Backpropagation
"""
dL/dL = 1.0 # Derivative of L w/r to L

L = d * f
dL/dd = f # Derivative of L w/r to d
Derived derivative:
(f(x+h) - f(x))/h # In this case 'x' is 'd'
((d+h)*f - d*f)/h
(df + hf - df)/h
hf/h = f

From above get derivates of L for d and f
L = d * f --> dL/dd = f
L = d * f --> dL/df = d

a -
    * - e -
b -         + - d (4.0|grad: -2.0) -
        c -                          * - L (-8.0|grad: 1.0)
                f (-2.0|grad: 4.0) -
"""

"""
Chain Rule Intuitive explanation:
'As put by George F. Simmons:
"If a car travels twice as fast as a bicycle and the bicycle is four
times as fast as a walking man, then the car travels 2 × 4 = 8 times
as fast as the man.'

dz/dx = dz/dy * dy/dx
So given above explanation you have the following:
    z --> car
    y --> bike
    x --> man
    dz/dy = 2, dy/dx = 4, then dz/dx = dz/dy * dy/dx = 2 * 4 = 8

Now use chain rule to get derivatives of L for c and e
Find the local gradient of d w/r to c (dd/dc):
d = c + e
Derived derivative:
(f(x+h) - f(x))/h # In this case 'x' is 'c'
((c+h) + e - c - e)/h
(c + h + e - c - e)/h
h/h = 1.0
thus, dd/dc = 1.0 and dd/de = 1.0
then applying chain rule for dL/dc = (dL/dd) * (dd/dc) = -2.0 * 1.0 = -2.0
thus the plus sign just passes through the gradient to the next node.

a -
    * - e (-6.0|grad: -2.0) -
b -                           + - d (4.0|grad: -2.0) -
        c (10.0|grad: -2.0) -                          * - L (-8.0|grad: 1.0)
                                  f (-2.0|grad: 4.0) -
"""

"""
Now applying chain rule for final nodes:
e = a * b
(f(x+h) - f(x))/h # In this case 'x' is 'a'
((a+h)*b - (a * b))/h
(ab + hb - ab)/h
hb/h = b
thus, de/da = -3.0 and de/db = 2.0
then dL/da = (dL/de) * (de/da) = -2.0 * -3.0 = 6.0
and dL/db = (dL/de) * (de/db) = -2.0 * 2.0 = -4.0
a (2.0|grad: 6.0)   -
                      * - e (-6.0|grad: -2.0) -
b (-3.0|grad: -4.0) -                           + - d (4.0|grad: -2.0) -
                          c (10.0|grad: -2.0) -                          * - L (-8.0|grad: 1.0)
                                                    f (-2.0|grad: 4.0) -
"""
