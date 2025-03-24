# Задача 5. Операция секретного кода


import re

code = input('Введите код: ')

def process_secret_code(code):
    code = code.replace(' ', '')

    if not re.fullmatch(r'[\d+\-*/.]+', code):
        if re.search(r'[^\d+\-*/.\s]', code):
            raise ValueError("Некорректный ввод данных. Введите только числа и операторы.")
        else:
            raise ValueError("Некорректный формат ввода. Допустимые операторы: +, -, *, /.")

    try:
        result = eval(code) # Используем eval, так как выражение арифметическое
        if not isinstance(result, (int, float)):
            raise TypeError("Некорректный формат кода. Невозможно выполнить операцию.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Ошибка: Деление на 0 недопустимо.")
    except Exception:
        raise TypeError("Некорректный формат кода. Невозможно выполнить операцию.")

    return result

try:
    print(process_secret_code(code))
except (ValueError, TypeError, ZeroDivisionError) as error:
    print(error)

