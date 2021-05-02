# Unlimited positional arguments
# *args by convention
# Positional arguments available as tuple

def add(*args):
    total = 0
    for arg in args:
        total += arg

    return total


# Unlimited Keyward Arguments
# **kwargs by convention
# Keyword arguments presented as dictionary

def calculate(n, **kwargs):
    
    n += kwargs['add']
    n *= kwargs['mult']

    return n


# EXAMPLE: Object initalization
# get() method gets specified keyword arg; returns None if undefined

class Car:

    def __init__(self, **kw):

        self.make = kw.get('make')
        self.model = kw.get('model')
