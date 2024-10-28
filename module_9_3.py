first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка с использованием zip
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))

# Генераторная сборка без использования zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result)) # Вывод: [1, 2]
print(list(second_result)) # Вывод: [False, False, True]
