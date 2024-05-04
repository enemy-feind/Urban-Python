def dictin(d):
    number = 0
    for i in d:
        number = number + len(i) + d[i]
    return number


def calculate_structure_sum(structure):
    number = 0
    for i in structure:
        if isinstance(i, int):
            number = number + i
        elif isinstance(i, str):
            number = number + len(i)
        elif isinstance(i, list):
            number = number + calculate_structure_sum(i)
        elif isinstance(i, dict):
            number = number + dictin(i)
        elif isinstance(i, set):
            number = number + calculate_structure_sum(i)
        elif isinstance(i, tuple):
            number = number + calculate_structure_sum(i)
    return number


data_structure = [
    [1, 2, 3],  # 6
    {'a': 4, 'b': 5},  # +11 = 17
    (6, {'cube': 7, 'drum': 8}),  # +6 +23 = +29 =46
    "hello",  # +5 = 51
    ((), [{(2, 'Urban', ('Urban2', 35))}])  # +0 +2 +5 +6 + 35 = 99
]
result = calculate_structure_sum(data_structure)
print(result)  # !99
