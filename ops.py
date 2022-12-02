def add(x,y):
	return x+y

def subtract(x,y):
	return x-y

def multiply(x,y):
	return x*y

def divide(x,y):
	return x/y

def modulo(x,y):
	return x%y

def GCD(x,y):
	if(y==0):
		return x
	else:
		return GCD(y, x%y)
