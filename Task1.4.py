# 1.4[8]. Требуется определить,
# можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Примеры/Тесты:
# 3 2 4 -> yes
# 3 2 1 -> no

n_slice = int(input('Введите кол-во n долек '))
m_slice = int(input('Введите кол-во m долек '))
count_brokenslice = int(input('Сколько долек хотите отломить? '))

if n_slice * m_slice > count_brokenslice and (count_brokenslice % n_slice == 0 or count_brokenslice % m_slice == 0):
    print('YES')
else:
    print('NO')

print('yes'if n_slice * m_slice > count_brokenslice and
(count_brokenslice % n_slice == 0 or count_brokenslice % m_slice == 0) else 'no')
