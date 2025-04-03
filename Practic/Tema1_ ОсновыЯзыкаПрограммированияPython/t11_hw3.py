# Задача 3. Калькулятор

class Calculator:

    def __init__(self):
        self.current_value = 0

    def set_value(self, value):
        self.current_value = value

    def get_value(self):
        return self.current_value

    def add(self, number):
        self.current_value += number

    def subtract(self, number):
        self.current_value -= number

    def multiply(self, number):
        self.current_value *= number

    def divide(self, number):
        if number == 0:
            print("Ошибка: Деление на ноль!")
        else:
            self.current_value /= number


# Пример использования класса Calculator
if __name__ == "__main__":
    calc = Calculator()

    calc.set_value(15)
    print("Текущее значение:", calc.get_value())

    calc.add(5)
    print("После сложения + 5:", calc.get_value())

    calc.subtract(3)
    print("После вычитания - 3:", calc.get_value())

    calc.multiply(2)
    print("После умножения на 2:", calc.get_value())

    calc.divide(4)
    print("После деления на 4:", calc.get_value())

    print("Результат деления на 0")
    calc.divide(0)  # Ошибка: Деление на ноль!
