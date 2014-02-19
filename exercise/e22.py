def is_odd(num):
	if num % 2 == 0:
		return False
	else:
		return True

def largest_odd(x,y,z):
	lt = x
	if x < y :
		lt = y
	if lt < z:
		lt = z
	if is_odd(lt):
		print lt
	else:
		print "the largest number is not odd"

def largest_odd24():
	