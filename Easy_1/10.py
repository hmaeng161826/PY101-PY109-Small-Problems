#write a function with one argument(number)
#function should return the result
#result = sum of all numbers between 1 and the argument that are multiples of
#3 or 5

#function name should be multisum(number)
#multiples of 3 or 5 numbers that can be divided by 3 or 5 without a remainder
#multiples should be smaller that the argument number

def multisum(number):
    summed_numbers = 0
    for num in range(1, number + 1):
        if num % 3 == 0:
            summed_numbers += num
        elif num % 5 == 0:
            summed_numbers += num
    return summed_numbers

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)