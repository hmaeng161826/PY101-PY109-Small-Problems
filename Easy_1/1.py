def odd_or_not(int):
    if int > 0:
        if int % 2 == 1:
            return True
        else:
            return False
    else:
        if (int * -1) % 2 == 1:
            return True
        else: 
            return False

print(odd_or_not(3))
print(odd_or_not(4))
print(odd_or_not(0))
print(odd_or_not(-1))
print(odd_or_not(-2))



#2nd attempt#

def odd_or_not(number):
    if abs(number) % 2 == 1:
        return True
    
#3rd attempt#

def odd_or_not(number):
    return abs(number) % 2 == 1


