# 6.2[32]: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца, т.е. функцию двух аргументов.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы.
# Примеры/Тесты:
# print_operation_table(lambda x,y: x**y,4,4)
# 1   1   1   1
# 2   4   8  16
# 3   9  27  81
# 4  16  64 256

# print_operation_table(lambda x,y: x*y)
# 1   2   3   4   5   6
# 2   4   6   8  10  12
# 3   6   9  12  15  18
# 4   8  12  16  20  24
# 5  10  15  20  25  30
# 6  12  18  24  30  36

def print_operation_table(func, num_rows = 6, num_columns = 6):
    lst1 = []
    print('    ', end='')
    for i in range(1,num_columns + 1):
        print(str(i).rjust(1), end=' ')
    print()
    print(' ', '_'*16)
    for i in range(1,num_columns + 1):
        print (i, '|', end= ' ')
        for j in range(1,num_rows + 1):
            lst1.append(func(i,j))
        print(' '.join(map(str,lst1)))
        lst1 = []

print_operation_table(lambda x, y: x**y, 4, 4)
print()
print_operation_table(lambda x,y: x*y)


# def print_operation_table(operation, num_rows=6, num_columns=6):
#     table = '\n'.join( list(map(lambda i: ''.join([f'{abs(operation(i, j)):<5}'
#                                     if j != 1 and i != 1 else f'{i:<5}'
#                                     if j == 1 else f'{j:<5}'
#                                     for j in range(1, num_columns + 1)]), range(1, num_rows + 1))))
#     print(table)

# print_operation_table(lambda x, y: x * y)