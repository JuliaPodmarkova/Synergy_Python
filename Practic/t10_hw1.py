# Задача 1. Подсчет гласных букв

word = (input("Введите строку: ").lower())

def count_vowels(word):
    try:
        if word.isalpha():
            count = 0
            vowels = set("aeiou")
            for letter in word:
                if letter in vowels:
                    count += 1
            return (f"Количество гласных букв в слове '{word}': {count}")
        else:
            raise ValueError('Слово должно состоять только из букв')
    except ValueError as e:
        return(f'{word} - {e}')

print(count_vowels(word))
