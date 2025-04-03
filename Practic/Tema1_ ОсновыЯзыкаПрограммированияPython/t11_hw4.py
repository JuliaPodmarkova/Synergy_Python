# Задача 4. Калькулятор 2.0

from t11_hw3 import Calculator
import math

class AdvancedCalculator(Calculator):

    def power(self, exponent):
        self.current_value **= exponent

    def square_root(self):
        if self.current_value < 0:
            print("Ошибка: Невозможно вычислить квадратный корень из отрицательного числа!")
        else:
            self.current_value = math.sqrt(self.current_value)



if __name__ == "__main__":
    adv_calc = AdvancedCalculator()

    adv_calc.set_value(25)
    print("Текущее значение:", adv_calc.get_value())

    adv_calc.square_root()
    print("Квадратный корень:", adv_calc.get_value())

    adv_calc.power(3)
    print("Возведение в степень 2:", adv_calc.get_value())

    adv_calc.set_value(-9)
    adv_calc.square_root()
