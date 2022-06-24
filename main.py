from decorator_logger import decorator_logger

@decorator_logger(path='logs.log')
def summator(a, b):
    return a + b

summator(3, 7)
summator(10, 70)
