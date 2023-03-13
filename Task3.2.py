# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным.
# Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

user_num = 9
list_num = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]

list_num.append(user_num)
list_num.sort()
if list_num.index(user_num) == len(list_num) - 1:
    print(list_num[list_num.index(user_num) - 1])
else:
    print(list_num[list_num.index(user_num) + 1])


