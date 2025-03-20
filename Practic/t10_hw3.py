# Задача 3. Путешествие по времени с ошибками

from datetime import datetime

print('Ваш друг, изобретатель по имени Доктор Глюк, создал машину времени.\nОн рассказывает, что машина способна отправить вас в прошлое или будущее')
print()
year = int(input('Для путешествия во времении введи год: '))

def time_travel(year):
    today_year = datetime.now().year
    try:
        if year > today_year and year % 2 != 0 and (year - today_year) < 100:
            return ('Путешествие во времени прошло успешно!')
        elif year < today_year:
            raise ValueError('Вы не можете путешествовать в прошлое!')
        elif year % 2 == 0:
            raise RuntimeError('Ой, что-то пошло не так! Машина времени сломана!')
        elif (year - today_year) >= 100:
            raise UserWarning('Машина времени предупреждает: выбранный год слишком далеко в будущем')
    except ValueError as v:
        return (f'{v}')
    except RuntimeError as r:
        return (f'{r}')
    except UserWarning as u:
        return (f'{u}')

print(time_travel(year))
