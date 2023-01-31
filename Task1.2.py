# 1.2[4]. Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Примеры/Тесты:
# 6 >>>  1  4  1
# 24 >>> 4  16  4
# 60 >>> 10  40  10
# s = x+x+4x

count_cranes = 12
min_cranes = 6
if count_cranes % min_cranes == 0:
    cranes_petia = cranes_sereja = count_cranes//min_cranes
    cranes_katia = (cranes_petia + cranes_sereja)*2
    print(f'{count_cranes} >>> Петя ({cranes_petia}) Катя ({cranes_katia}) Сережа ({cranes_sereja})')
else:
    print('Данное кол-во журавликов нельзя разделить по условию задачи')
