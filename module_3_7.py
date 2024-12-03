def calculate_structure_sum(n):
    summa = 0
    for item in n:
        if isinstance(item, (list, tuple, set)):
            summa += calculate_structure_sum(item)
        elif isinstance(item, dict):
            summa += calculate_structure_sum(item.items())
        elif isinstance(item, (int, float)):
            summa += item
        elif isinstance(item, str):
            summa += len(item)
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
