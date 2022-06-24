import datetime


def decorator_logger(path):

    def _logger(old_function):

        def new_function(*args, **kwargs):
            start = datetime.datetime.now()
            name_function = old_function.__name__
            result = old_function(*args, **kwargs)
            log = f'Дата и время вызова функции - {start}; ' \
                  f'имя функции - "{name_function}"; ' \
                  f'аргументы, с которыми вызвалась функция - {args} и {kwargs}; возвращаемое значение - {result}.\n'
            with open(path, 'a', encoding='Utf-8') as f:
                f.write(log)
            return result

        return new_function

    return _logger
