def calculate_structure_sum(structure) -> int:
    value = 0
    for i in structure:
        if not isinstance(i, int | str):
            value += calculate_structure_sum(i.items() if isinstance(i, dict) else i)
        else:
            value += i if isinstance(i, int) else len(i)
    return value


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
