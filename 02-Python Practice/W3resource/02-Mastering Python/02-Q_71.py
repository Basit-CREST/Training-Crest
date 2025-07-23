def first_common_sequence(str):
    ans = ""
    short = min(str,key=len)
    for i in range(len(short)):
        if all(x.startswith(short[:i+1]) for x in str):
            ans = short[:i+1]
        else:
            break
    return ans
lst = ["fly","flower","flow"]
print(first_common_sequence(lst))
