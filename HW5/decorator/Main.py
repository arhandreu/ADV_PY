import datetime


def create_log_path(path='logs.txt'):
    def create_log(func):
        def logs(*args, **kwargs):
            dt = datetime.datetime.today().replace(microsecond=0)
            value = func(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as logs:
                logs.write(f'Дата и время: {dt}\nИмя фунции: {func.__name__} | Аргументы: {args, kwargs} | Возврашаемое '
                           f'значение: {value}\n')
                logs.write('--'*25 + '\n')
            print('Лог записан')
            return value
        return logs
    return create_log


@create_log_path()
def function1(*args, **kwargs):
    return sum(args)


if __name__ == '__main__':
    function1(1, 2, 3, 4, a=123, b='Слово', с=["Список", "Слов"])