def sat(q,r):
	t=60*q+52*r
	g = 2452
	print "q=", q
	print "r=", r
	print t
	print
	if t > g:
		l = t-g
		print "you are too high"
		print t-g 
		print l/60,".", l%60, "/ by q"
		print l/52,".", 1%52 ,"/ by r"
	elif t<g:
		h = g-t
		print "you are too low"
		print g-t
		print h/60,".", h%60, "/ by q"
		print h/52,".", h%52, "/ by r"
	else:
		print "you got it"
	print

#sat(15,15) sat(20, 20)

sat(20, 21)

#sat(18, 22), sat (18, 23)


sat(14,31)

			