# Purpose:	Find the roots of a polynomial function via the bisection numerical method
# Author:	Massimo Penzo

# defining the function we are trying to find the roots for
def f(x):
	return x**6 - x - 1

# bisect algorithm implementation
def bisect_method(a, b, tolerance):

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

root = bisect_method(1, 2, 0.00005)
print(root)