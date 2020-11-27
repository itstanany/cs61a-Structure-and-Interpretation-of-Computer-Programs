""" Homework 1: Control """

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return h(a, b)']
    """
    if b >= 0:
        h = add
    else:
        h = sub
    return h(a, b)
# print(a_plus_abs_b(2, 3))
def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    a = 0
    b = 0
    if x <= y and y <= z :
        a = x
        b = y
    elif x <= y and z <= y:
        a = x
        b = z
    elif y <= x and x <= z:
        a = y
        b = x
    elif y <= x and z <= x:
        a = y
        b = z
    elif z <= x and x <= y:
        a = z
        b = x
    elif x <= z and z <= y:
        a = x
        b = z
    return add(a*a, b*b)
# print(two_of_three(1, 2, 3))
# print(two_of_three(5, 3, 1))
# print(two_of_three(10, 2, 8))
# print(two_of_three(5, 5, 5))
def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    if x%2 == 0:
        return x/2
    elif x%3 == 0:
        return x/3
    elif x%5 == 0:
        return x/5
    else:
        return 1


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return print(true_result)
    else:
        return print(false_result)


def with_if_statement():
    """
    >>> result = with_if_statement()
    6
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    5
    6
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    return True

def t():
    return 5 , 6

def f():
    return 5
result = with_if_function()
print(result)

def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    #record the length of the sequence
    seq_length = 0
    #loop through all x untill it is equal to x 
    #print the current x in seqence and increase sequence length by 1
    while x >= 1:
        seq_length += 1
        #print the current x and update it value to its half is it's even
        if x%2 ==0 or x ==1:
            print(x)
            x = x/2
        #if current value is odd, print it and use formula to update it
        else:
            print(x)
            x = 3*x + 1
    return seq_length
