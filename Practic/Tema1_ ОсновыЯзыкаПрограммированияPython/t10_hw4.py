# Задача 4. Числовая головоломка

import re

def solve_math_puzzle(puzzle):

    puzzle = puzzle.replace(' ', '')

    if not re.fullmatch(r'[\d\+\-\*\/\()\.$$$$$$\s]+$', puzzle):
        raise ValueError("В головоломке присутствуют некорректные символы или операции.")

    try:
        result = eval(puzzle)
        if not isinstance(result, (int, float)):
            raise TypeError("Невозможно выполнить преобразование типов.")
    except Exception:
        raise TypeError("Невозможно выполнить преобразование типов.")

    return result


line = input('Введите числа и математические символы через пробел: ')
try:
    print(solve_math_puzzle(line))
except (ValueError, TypeError) as e:
    print(e)
