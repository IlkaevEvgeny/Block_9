from typing import List, Any
from random import choice

# Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

compare_letters = lambda x, y: x == y if len(x) == len(y) else False
result = list(map(compare_letters, first, second))
print(result)

# Замыкание
def get_advanced_writer(file_name: str, encoding='utf-8'): # Добавлен аргумент encoding
    def write_everything(*data_set: Any):
        with open(file_name, 'a', encoding=encoding) as f: # Указана кодировка при открытии
            for i, data in enumerate(data_set):
                f.write(f'{i+1}. {data}\n')
    return write_everything

# Пример использования
write = get_advanced_writer('example.txt', encoding='utf-8')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод call
class MysticBall:
    def __init__(self, *words: str):
        self.words = words

    def __call__(self) -> str:
        return choice(self.words)

# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())