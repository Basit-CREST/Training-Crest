def fibonaci(s):
    #list_fib = [0]
 
    if s == 1 or s == 2:
        return 1
    else:
        return fibonaci(s-1) + fibonaci(s-2)

print(fibonaci(4))