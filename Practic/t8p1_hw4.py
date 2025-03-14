# Задача 4. Аргументирующий декоратор

def arg_decor(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            print(f'value = {arg} type = {type(arg)}')
        for key, value in kwargs.items():
            print(f'{key}={value}, {typr(value)}')
        return func(*args, **kwargs)
    return wrapper

@arg_decor
def some_func_1(a, b, c):
	print(f'{a}.{b}.{c}')

@arg_decor
def some_func_2(*cool_args):
    pass

print(some_func_1(3, 'Помидор', 3.14))
print()
print(some_func_2(3, 'Помидор', 3.14))
