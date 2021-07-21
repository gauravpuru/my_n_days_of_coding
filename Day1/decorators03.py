"""
Decorators in Python are very powerful which modify the behavior
of a function without modifying it permanently. It basically
wraps another function and since both the function are callable
, it returns a callable.
"""

def function1(function):
    def wrapper():
        print("Hello guarav Kumar")
        function()
        print("The function has been executed")
    return wrapper

@function1
def function2():
    print("This is a statement from a seperate function")

##    function1(function2)()

function2()