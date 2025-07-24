def even(come_here):
    ans = []
    for i in come_here:
        if i % 2 == 0:
            ans.append(i)
    return ans

print(even([1,2,3,4,5,6,7,8,9,10]))

