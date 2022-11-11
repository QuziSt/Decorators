# Доработать декоратор logger в коде ниже. Должен получиться декортор, который записывает в файл 'main.log' дату и время
# вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение. Функция test_1 в коде ниже также
# должна отработать без ошибок.
from datetime import datetime
import os


def logger(old_function):
    pass

    def new_function(*args, **kwargs):
        result = sum(args)
        with open('main.log', 'a') as main:
            now = datetime.now()
            main.write(str(now)+'\n')
            for arg in args:
                main.write(str(arg)+' ')
            main.write('\n')
            for kwarg in kwargs:
                result += kwargs[kwarg]
                main.write(str(kwargs[kwarg])+' ')
            main.write(str(result) + '\n')

            main.write('\n'+str(old_function.__name__)+'\n')
        return result

    return new_function


def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def summator(a, b=0):
        return a + b

    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()
