# Задача 2.Перевод в верхний регистр

def process_word(word):
    try:
        if word.isalpha():
            return word.upper()
        else:
            raise ValueError('Слово должно состоять только из букв')
    except ValueError as e:
        return (f'{word} - {e}')

word = input('Введите слово: ').lower()

print(process_word(word))
