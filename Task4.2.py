# 4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом.
# На входе задано количество ягод на каждом кусте. Не обязательно вводить их с клавиатуры,
# можно задать непосредственно в коде программы

# Примеры/Тесты:
# Input1: 1, 2, 3, 4, 5, 6, 7, 8
# Output1: Макс. кол-во ягод 21, собрано для куста 7

# Input1: 11, 92, 1, 42, 15, 12, 11, 81
# Output1: Макс. кол-во ягод 184, собрано для куста 1

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
list_1 = [11, 92, 1, 42, 15, 12, 11, 81]
sum = 0
for idx in range(len(list_1)):
    idx_next = idx+1 if idx != len(list_1) - 1 else idx - len(list_1) + 1
    sum_current = list_1[idx-1] + list_1[idx] + list_1[idx_next]
    if sum_current > sum:
        sum = sum_current
        find_idx = idx + 1
print(f'Макс. кол-во ягод {sum}, собрано с куста {find_idx}')
