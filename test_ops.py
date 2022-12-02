from ops import *

def test_add():
	assert add(2,3) == 5
	assert add(2,-3) == -1
	assert add(-2,-3) == -5

def test_subtract():
	assert subtract(2,3) == -1
	assert subtract(3,2) == 1
	assert subtract(-2,3) == -5
	assert add(-2,-3) == 1

def test_multiply():
	assert multiply(2,3) == 6
	assert multiply(-2,-3) == 6
	assert multiply(2,-3) == 6

def test_divide():
	assert divide(10,5) == 2
	assert divide(10,-5) == 2
	assert divide(-10,-5) == 2

	
def test_modulo():
	assert modulo() == 
	assert 

def test_power():
	assert power(2,2) == 4
	assert power(2,-2) == 0.25
	assert power(-2,-2) == 0.25
	assert power(-2,3) == 0.25
