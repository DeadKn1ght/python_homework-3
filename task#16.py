# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# пример:
# 5
# 1 2 3 4 5
# 3
# -> 1

array = []
N = int(input('Input lenghght of your array "N" : '))
for i in range(1,N) :
    array.append(i)
print(f'Your array is : {array}')
X = int(input('Input number "X" that you will find in yor array : '))
count = 0
for i in range(len(array)):
    if array[i] == X :
        count += 1
print(f'Number "X" appears in your array {count} times')