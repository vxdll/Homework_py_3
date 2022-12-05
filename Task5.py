# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input("Введите k: "))
i = 0
f_0 = 0
f_1 = -1
result = [f_0, f_1]

while i < k - 1:
    sum_fib = f_0 + f_1
    f_0 = f_1
    f_1 = sum_fib
    result.append(sum_fib)
    i += 1

result = list(reversed(result))
f_1 = 1
f_0 = 0
j = 0
result.append(f_1)

while j < k - 1:
    sum_fib_2 = f_0 + f_1
    f_0 = f_1
    f_1 = sum_fib_2
    result.append(sum_fib_2)
    j += 1

print(result)
