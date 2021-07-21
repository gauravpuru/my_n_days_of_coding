import functools

def repeat(num):
    def decorators_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num):
                value = func(*args,**kwargs)
            return value
        return wrapper
    return decorators_repeat

@repeat(num=5)
def funstion(name):
    print(f"{name}")

funstion("Gaurav")