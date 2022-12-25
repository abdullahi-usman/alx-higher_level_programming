#!/usr/bin/python3

"""Add Integer Module """
def add_integer(a, b=98):
	"""Add two integers and return their result"""
	if (type(a) not in [int, float]):
		raise TypeError('a must be an integer')
	if (type(b) not in [int, float]):
		raise TypeError('b must be an integer')
	return (a + b)
