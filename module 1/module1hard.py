def average(entry):  # Получение среднего значения
    n = 0
    for i in entry:
        n = n + i
    n = n / len(entry)
    return n


def take_name(names):
    name = 'z'
    for i in names:
        if i < name:
            name = i
    return name


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
result = {}

for i in grades:
    thing = take_name(students)
    students.discard(thing)
    result[thing] = average(i)
print(result)
