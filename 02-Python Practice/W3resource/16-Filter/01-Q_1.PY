l = [1,10,20,30,56,78,33,100]

print(list(filter(lambda x : x % 10 == 0 , l)))



def find_single_digit(x):
    return len(str(x)) == 1
        
l = [1,10,20,30,56,78,33,100]

print(list(filter(find_single_digit, l)))


