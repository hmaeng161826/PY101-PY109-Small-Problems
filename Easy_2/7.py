#write an xor function(argum1, argum2): 
#RETURNS True IF: only one argument is truthy. 
#RETURNS False otherwise (else)

def xor(argum1, argum2):
    if not (argum1 and argum2):
        return True
    else:
        return False

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

#2nd attempt

def xor(argum1, argum2):
    if (argum1 and not argum2) or (argum2 and not argum1):
        return True
    return False
