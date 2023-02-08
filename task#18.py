# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# пример:
# 5
# 1 2 3 4 5
# 6
# -> 5
array = []
N = int(input('Input lenghght of your array "N" : '))
for i in range(1, N+1):
    array.append(i)
print(f'Your array is : {array}')
X = int(input('Input number "X" : '))
for i in range(len(array)):
    if array[i] == X:
        print(f'The most equal element of your array to number "X" is : {array[i]}')
if (X < 1):
    print(f'The most equal element of your array to number "X" is : 1')
if (X > len(array)):
    print(f'The most equal element of your array to number "X" is : {len(array)}')
