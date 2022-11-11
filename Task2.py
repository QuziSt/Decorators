# Доработать парметризованный декоратор logger в коде ниже. Должен получиться декортор, который записывает в файл дату и
# время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение. Путь к файлу должен
# передаваться в аргументах декоратора. Функция test_2 в коде ниже также должна отработать без ошибок.

from datetime import datetime
import os


def logger(path):

    def __logger(old_function):
        def new_function(*args, **kwargs):
            res = 0
            result = 0
            with open(f'{path}', 'a') as new_log:
                for kwarg in kwargs:
                    result += kwargs[kwarg]
                    new_log.write(str(kwargs[kwarg]) + ' ')
                for arg in args:
                    result += arg
                    new_log.write(str(arg) + ' ')
                now = datetime.now()
                new_log.write(old_function.__name__)
                new_log.write(str(now))
                new_log.write(str(result) + '\n')
            return result
        return new_function

    return __logger



def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        div(4, 2)
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()
