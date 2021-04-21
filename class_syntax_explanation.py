

# Make a class named X that is-a Y."
class X(Y)
class X(object):
    def __init__(self, J)   '''Class X has-a __init__ that takes
'self' and 'J' parameters.'''

class X(object):
    def M(self, J) '''Class X has-a function named M that takes self
and J parameters.'''

foo = X() '''Set 'foo' to an instance of class X.'''

foo.M(J)  '''From 'foo', get the  K attribute, and set it to Q.'''



'''In each of these, where you see X, Y, M, J, K, Q, and foo, you can treat those like blank spots.

For example, I can also write these sentences as follows:

1. “Make a class named ??? that is-a Y.”
2. “class ??? has-a __init__ that takes self and ??? parameters.”
3. “class ??? has-a function named ??? that takes self and ??? parameters.”
4. “Set ??? to an instance of class ???.”
5. “From ???, get the ??? function, and call it with self=??? and parameters ???.”
6. “From ???, get the ??? attribute, and set it to ???.”
'''
