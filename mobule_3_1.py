# Глобальная переменная для подсчета вызовов
calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return (length, upper, lower)
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    # Приводим строку к нижнему регистру для сравнения
    string_lower = string.lower()
    # Проверяем, содержится ли строка в списке (все элементы также приводим к нижнему регистру)
    return any(string_lower == item.lower() for item in list_to_search)
# Примеры вызова функций
print(string_info('Capybara'))  # (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  # (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycling', 'cyclic']))  # False
# Выводим количество вызовов
print(calls)  # Выводит общее количество вызовов
