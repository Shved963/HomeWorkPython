# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя

# 	Примеры/Тесты:
#     <function_name>(0,0) -> 0
#     <function_name>(0,2) -> 2
#     <function_name>(3,0) -> 3

def sum_func(a, b):
    if b == 0:
        return a
    return sum_func(a+1, b-1)

print(sum_func(0, 0))
print(sum_func(0, 2))
print(sum_func(3, 0))