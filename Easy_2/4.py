def multiply(num1, num2):
    return num1 * num2

def square(num):
    return multiply(num, num)

# further exploration
# power to the n = number * number * number ...
# iterate n times

#not using multiply function
def power_to_the_n(number, n):
    exponent = 1
    for _ in range(n):
        exponent *= number
    return exponent

#using multiply function
def power_to_the_nth(number, n):
    result = 1
    for _ in range(n):
        result = multiply(number, result)
    return result

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

print(power_to_the_n(3, 6))
print(power_to_the_nth(3, 6))
