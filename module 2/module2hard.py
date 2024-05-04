def repeat_check(results, first, second):  # Проверка на повторы
    ln = len(results)
    if ln == 0:
        return True
    item = 2
    while item <= ln:
        if results[item - 1] == first and results[item - 2] == second:
            return False
        item += 2
    return True


def multiple_check(number, first, second):  # Проверка на кратность
    if first == 0 or second == 0 or first == second:
        return False
    if (number % (first + second)) == 0:
        return True


n = 0
while n < 3 or n > 20:
    print('Enter number between 3 or 20 ', end='')
    n = int(input())
result = []
for i in range(n):
    for y in range(n):
        if multiple_check(n, i, y):
            if repeat_check(result, i, y):
                result.append(i)
                result.append(y)
print('For number ', n, ' Result is ', *result, sep='')
