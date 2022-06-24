from itertools import chain
from decorator_logger import decorator_logger

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

nested_list2 = [
    ['a', ['b', 'c']],
    ['d', ['e', 'f', ['h', False]]],
    [[1, 2], None]
]


@decorator_logger(path='logs.log')
def flat_generator(my_list):
    for l in my_list:
        for i in l:
            yield i


@decorator_logger(path='logs.log')
def flat_generator2(my_list):
    for l in my_list:
        if isinstance(l, list):
            for i in flat_generator2(l):
                yield i
        else:
            yield l


if __name__ == '__main__':

    for item in flat_generator(nested_list):
        print(item)
    print('*' * 40)
    for item in flat_generator2(nested_list2):
        print(item)
