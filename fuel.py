def calculate_fuel_percentage(fraction_str):
    while True:
        try:
            x, y = map(int, fraction_str.split('/'))
            if y == 0 or x > y:
                raise ValueError

            percentage = (x / y) * 100
            if percentage <= 1:
                return 'E'
            elif percentage >= 99:
                return 'F'
            else:
                return str(round(percentage)) + '%'
        except ValueError:
            fraction_str = input("Некорректный ввод. Пожалуйста, введите дробь в формате x/y, где x и y - целые числа, и x <= y: ")
        except ZeroDivisionError:
            fraction_str = input("Деление на ноль невозможно. Пожалуйста, введите новое значение: ")

if __name__ == '__main__':
    fraction = input("Дробь: ")
    result = calculate_fuel_percentage(fraction)
    print(result)
