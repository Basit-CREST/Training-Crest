def get_parentheses_depths(groups_string):
    groups = groups_string.split()
    depths = []
    
    for group in groups:
        count = 0
        max_depth = 0
        for char in group:
            if char == '(':
                count += 1
                max_depth = max(max_depth, count)
            elif char == ')':
                count -= 1
        depths.append(max_depth)
    
    return depths

input_str = "(()) (()) () ((()()()))"
result = get_parentheses_depths(input_str)
print(result)
