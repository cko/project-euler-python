

def euclid(a,b):
	if b == 0:
		return a
	else:
		return euclid(b, a % b)