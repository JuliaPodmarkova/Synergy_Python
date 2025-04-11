class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        if self.count / self.size >= 0.7:
            self.resize()
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.count += 1

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Если ключ не найден

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.count -= 1
                return True
        return False  # Если ключ не найден

    def resize(self):
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]
        for bucket in self.table:
            for key, value in bucket:
                new_index = hash(key) % new_size
                new_table[new_index].append((key, value))
        self.table = new_table
        self.size = new_size

def string_hash(s):
    return sum(ord(char) for char in s)

def create_string_dict(strings):
    string_dict = {}
    for s in strings:
        string_dict[s] = string_hash(s)
    return string_dict

print("______________________________________________")
if __name__ == "__main__":
    print("Проверяем функцию, которая принимает строку и возвращает её хеш-значение")
    print()
    strings = ["Привет мир", "Мир", "Труд", "Май", "Жвачка", "Синергия"]
    print(f'Строка для работы функции: {strings}')
    print()
    string_dict = create_string_dict(strings)

    for s in strings:
        print(f"Строка: '{s}', Хэш: {string_dict[s]}")

    print("______________________________________________")
    print('Работа с хэш-таблицей')
    print()

    ht = HashTable(5)
    ht.insert('key0', 1)
    ht.insert('key1', 2)
    ht.insert('key2', 3)
    ht.insert('key3', 4)
    ht.insert('key4', 5)
    ht.insert('key5', 6)
    ht.insert('key6', 7)
    ht.insert('key7', 8)
    ht.insert('key8', 9)
    ht.insert('key9', 10)
    print(f'Добавлено ключей - {ht.count}')
    print(f"Размер хэш-таблицы до изменения размера: {ht.size}")
    print("______________________________________________")
    print()
    print('Проверяем работу автоматического увеличения хэш-таблицы, добавляем еще 6 ключей')
    print()
    ht.insert('key10', 11)
    ht.insert('key11', 12)
    ht.insert('key12', 13)
    ht.insert('key13', 14)
    ht.insert('key14', 15)
    ht.insert('key15', 16)

    print(f'Всего ключей добавлено - {ht.count}')
    print(f"Размер хэш-таблицы до изменения размера: {ht.size}")
    print("______________________________________________")
    print()

    ht.resize()

    print(f"Размер хэш-таблицы после ручного изменения размера: {ht.size}")
    print(f'Всего ключей - {ht.count}')
    print("______________________________________________")
    print(f'Поиск ключей. Добавлено {ht.count} ключей. Ищем в диапазоне "range(20)".S')
    print()

    for i in range(20):
        print(f"Поиск 'key{i}': {ht.search(f'key{i}')}")
    print("______________________________________________")