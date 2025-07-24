from itertools import accumulate,chain

l1 = [1,2,3,4,5,6]
l2 = ["a","b","c","d","e"]
l3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def acc(a1,a2,a3):
    
    return chain(a1,a2,a3)

ans = list(acc(l1,l2,l3))
print(type(ans))
print(ans)


def sum(a):
    return accumulate(a)

print(list(sum(l1)))