def add(a, b):
    """
    Adds two numbers
    :param a: a number
    :param b: a number
    :return:  the sum of the numbers
    """
    return a + b

def subtract(a, b):
    return a-b

def magic(x):
    if(x < 0):
        return None
    return 1 if x==0 else x*magic(x-1)