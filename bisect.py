# Purpose:	Find the roots of a polynomial function via the bisection numerical method
# Author:	Massimo Penzo

# defining the function we are trying to find the roots for
def f(x):
	return x**2 - 2

# bisect algorithm implementation
def bisect(a, b, tolerance):

	c = (a + b) / 2
	while (b - a) / 2 > tolerance:

		if f(a)*f(c) > 0:
			a = c
		elif f(a)*f(c) < 0:
			b = c
		else :
			return c
		c = (a + b) / 2
		
	return c	

root = bisect(-100, 100, 0.0003)
print(root)