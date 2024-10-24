
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple)):
            raise TypeError
        total_sum, incorrect_data = personal_sum(numbers)
        count = len(numbers) - incorrect_data  # Учитываем некорректные данные
        return total_sum / count if count > 0 else 0
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

# Вызовы функции calculate_average с различными данными
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Некорректный тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # 4
print(f'Результат 3: {calculate_average(567)}')  # Некорректный тип
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # 26.5