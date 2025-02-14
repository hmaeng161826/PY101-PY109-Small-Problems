#function(number)
#if number > 0 (positive): return negative of that number(* -1)
#else: return number

def negative(number):
    if number > 0:
        return number * -1
    else:
        return number

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True

#2nd attempt
#the ultimate goal is to negate the number. 

def negative(number):
    return -abs(number)

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True