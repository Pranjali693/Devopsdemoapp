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

