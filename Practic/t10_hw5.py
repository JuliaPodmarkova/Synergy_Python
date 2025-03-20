# Задача 5. Операция секретного кода

import re

code = input('Введите код: ')

def process_secret_code(code):
    code = code.replace(' ', '')

    if not re.fullmatch(r'[\d\+\-\*\/\.$$$$$$\s]+$', code):
        raise ValueError("Некорректный формат ввода. Допустимые операторы: +,-,*,/.")
    try:
        result = eval(code)
        if not isinstance(result, (int, float)):
            raise AttributeError("Некорректный формат кода. Невозможно выполнить операцию.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Некорректный формат кода. Деление на 0 недопустимо.")
    except Exception:
        raise TypeError("Некорректный формат кода. Невозможно выполнить операцию.")

    return result

try:
    print(process_secret_code(code))
except (ValueError, TypeError, ZeroDivisionError, Exception, AttributeError) as error:
    print(error)


