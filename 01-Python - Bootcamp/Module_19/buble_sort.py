### buble sort
my_arr = [2,8,4,5,6,10,1]
bol = 0
for i in range(len(my_arr)-1):
    swapped = False
    for j in range(len(my_arr)-i-1):
        if my_arr[j] > my_arr[j+1]:
            my_arr[j] = my_arr[j] ^ my_arr[j+1]
            my_arr[j+1] = my_arr[j] ^ my_arr[j+1]
            my_arr[j] = my_arr[j] ^ my_arr[j+1]
            swapped = True
        
    if not swapped :
        break 

for i in my_arr:
    print(i)