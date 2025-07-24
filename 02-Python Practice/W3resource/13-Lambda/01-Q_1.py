input = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
ans = sorted(input , key =  lambda x : x[1], reverse= True)
print(ans)   


input.sort(key = lambda x : x[1])
print(input)