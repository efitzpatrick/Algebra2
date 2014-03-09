#p = input("What is the perimeter length?")
p = 60000
p = int(p)
e = int(p/2)

#create a blank dictionary
a = {}

for x in range(0,e):
	y = e - x
	area = x * y
	tooMuch = x + y
	if tooMuch > e:
		print ("Done")
		break
	else:
		#print ( x, '*', y, '=', area)
		a[area] = x, y
		#print (a)

maxiumum = max(a.keys(), key=int)

print ("Your maximum area is ", maxiumum,". Which is gotten to by multiplying", a[maxiumum], "!")
