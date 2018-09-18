# -*- coding: utf-8 -*-
# a = [[1,5,-1,7], [2,-1,-1,4], [3,-2,4,11]]
# n = 3
print('Здравствуйте')
n = int(input('Введите количество строк матрицы: '))

print('Введите СЛАУ в матричном виде')
a = [[0 for j in range(n+1)] for i in range(n)]  # двумерный массив заполненный нулями
for i in range(n):
    for j in range(n+1):
        if j == n:
            message = 'b' + str(i + 1)
            a[i][j] = int(input(message + ' '))
        else:
            message = 'a' + str(i + 1) + str(j + 1)
            a[i][j] = int(input(message + ' '))

# Прямой ход алгоритма

for k in range(1, n):
    for j in range(k, n):
        m = a[j][k-1] / a[k-1][k-1]
        for i in range(n+1):
            a[j][i] = a[j][i] - m * a[k-1][i]

# Обратный ход

x = [0 for i in range(n)]  # список полученных коэффициентов
for i in range(n-1, -1, -1):
    x[i] = a[i][n] / a[i][i]
    for c in range(n-1, i, -1):
        x[i] = x[i] - a[i][c] * x[c] / a[i][i]

result = 'Результат: '
for i in range(n):
    result = result + 'x' + str(i + 1) + '=' + str(x[i]) + '; '

print (result)