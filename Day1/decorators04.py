def function1(function):
    def wrapper(*args, **kwargs):
        print("hello there")
        function(*args,**kwargs)
        print("Welcome to python programming")
    return wrapper

@function1
def function2(name):
    print(f"{name}")

function2('Gaurav Kumar')