def find_positions(data, target):
    result = [
        [[i, j] for j in range(len(data[i])) if data[i][j] == target]
        for i in range(len(data)) if target in data[i]
    ]
    return result

input_data = ([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19])
target_value = 19

positions = find_positions(list(input_data), target_value)
print(positions)
