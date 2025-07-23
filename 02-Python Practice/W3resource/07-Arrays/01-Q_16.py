def pattern(colors, patterns):
    if len(colors) != len(patterns):
        return False

    p_to_c = {}  
    c_to_p = {}  

    for color, pattern in zip(colors, patterns):
        
        if pattern in p_to_c:
            if p_to_c[pattern] != color:
                return False
        else:
            p_to_c[pattern] = color

       
        if color in c_to_p:
            if c_to_p[color] != pattern:
                return False
        else:
            c_to_p[color] = pattern

    return True


color1 = ["red", "red", "green"]
patterns = ["a", "b", "a"]

print(pattern(color1,patterns))

