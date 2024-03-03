def greet(fx):
    def mfx(*args,**kwargs):
        print('You are welcome in this function')
        fx(*args,**kwargs)
        print("Thank you for using this function")
    return mfx  
@greet
def hello():
    print("Welcome in python programming")  

hello()
@greet
def avg(a,b,c):
    print ((a+b+c)/3)

avg(3,4,5)

import logging
def log_function_call(func):
    def decorated(*args,**kwargs):
        logging.info(f'Calling {func.__name__} with arg={args} ,kwargs={kwargs}')
        result=func(*args,**kwargs)
        logging.info=(f'{func.__name__} returned {result}')
        return result
    return decorated
@log_function_call
def sum(a,b):
    print (a+b)

sum(234,456)

                     


  