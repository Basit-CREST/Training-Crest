def divideer(arr,k):

    if len(arr) > k and len(arr) % k:
        return True
    else:
        return False


list = [1, 2, 3, 4, 5, 6, 7]
number = 4

print(divideer(list,number))