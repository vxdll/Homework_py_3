# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

def ten_in_doble(n):
    lst = ""
    while n > 0:
        x = str(n % 2)
        lst = x + lst
        n = n // 2
    return lst
print(ten_in_doble(45))