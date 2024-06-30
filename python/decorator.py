import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log(func):
    def wrapper(*args,**kwargs):
        logging.info(f"start calling function {func.__name__}")
        result=func(*args,**kwargs)
        logging.info(f"end calling function {func.__name__} return:{result}")
        return result
    return wrapper

@log
def add(a,b,c):
    return a+b+c

@log
def multiple(b,a=3):
    return a*b

add(1,2,3)
multiple(6,5)
    