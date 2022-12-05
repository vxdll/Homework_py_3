# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

# Создадим цикл for при помощи его заполним список
a, b = int(input("Введите a = ")), int(input("Введите b = "))
lst = []
for i in range(a,b):
    n = int(input("Введите значение элемента х = "))
    lst.append(n)

mult = 1
i = 0
new_lst = []
while i < len(lst)/2:
    if len(lst) % 2 == 0:
        mult = lst[i] * lst[(len(lst)) - i - 1]
        new_lst.append(mult)
        i += 1
    else:
        if lst[i] != lst[(len(lst))//2]:
            mult = lst[i] * lst[(len(lst)) - i - 1]
            new_lst.append(mult)
            i += 1
        else:
            mult = lst[(len(lst))//2] ** 2
            new_lst.append(mult)
            i += 1

print(new_lst)


