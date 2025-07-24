MY_LIST = [1,2,3,4,56,7,8,8,9,10]


ans = list(map (lambda x : x ** 2, MY_LIST))
print(ans)


dict = { "subject" : [10,20,30,40,50] , "language" : [90,80,70,60,50]}

ans = list(zip(*[[(i,val) for val in j] for i , j in dict.items()]))
print(ans)