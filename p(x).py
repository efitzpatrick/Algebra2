def funcMath(x):
	c = 4*x**5
	c = c-3*x**4
	c = c +2*x**3
	c = c-7*x**2
	c = c +9*x-5
	return c

	#print (c)

for i in range (-10,10):
	b = funcMath(i)

	print ("f(",i,") = ", b)