def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError:
        print(a, b)


add_everything_up(1, '2')   # задаём переменые здесь
