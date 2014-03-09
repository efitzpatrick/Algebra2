import sys
c = .5
for x in range(1,15):
	b = x + (15 - x)
	if b > 15:
		print ("Done")
		break
	else:	
		a = (15-x)*x
		print ( x, '*', (15-x), '=', )