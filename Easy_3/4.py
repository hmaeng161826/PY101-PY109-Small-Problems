#function(positive integer):
    #returns a string
    #string length = arugment integer
    #string altenates 1 and 0
#ex): 3: 101 5:10101 6: 101010 
#if 0 or negative: raise error

#prints 1 and 0 continuously upto the number of the argument
#iterate argument(n) times and each iteration print 1 at first and if previous
#output was 0 , and print 0 if previous output was 1.


def stringy(length):
    string = '1'
    previous_string = '1'
    for _ in range(1, length):
        if previous_string == '1':
            string += '0'
            previous_string = '0'
        elif previous_string == '0':
            string += '1'
            previous_string = '1'
    return string
        
print(stringy(6))
print(stringy(9))
print(stringy(4))
print(stringy(7))

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True

#2nd attempt

def stringy(length):
    string = ""
    for idx in range(length):
        if idx % 2 == 0:
            string += '1'
        elif idx % 2 == 1:
            string += '0'
    return string
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True