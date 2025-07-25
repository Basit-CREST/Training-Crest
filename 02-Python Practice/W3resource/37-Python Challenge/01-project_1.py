## add digits till we get single digit

def machine(i):

    while (i // 10) > 0:

        temp = i
        sum = 0 
        while temp:

            sum += temp % 10
            temp = temp // 10
        
        i = sum
    return i

print(machine(999))

