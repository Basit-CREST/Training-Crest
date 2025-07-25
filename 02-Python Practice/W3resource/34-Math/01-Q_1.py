import math

def sum_of_base_to_the_power(base,power):
    return sum([int(i) for i in str(pow(base,power))])


print(sum_of_base_to_the_power(5,2))
