#function(year):
    #return string; (string = begins with the century number ex)21st 23rd etc)
    #print st: 1,  (everything ends with 1 except 11 exception)
#nd: 2 22  everything ends with 2 except 12 exception
#rd: 3 23  everything ends with 3 except 13 exception
#th: 0, 4, 5, 6, 7, 8, 9 11 12 13 14 15 16 17 18 19
#20 24 25  everything else including exception
# if century_number <= 10: look for last substring 
#if century_number  > 10, <14: th 
#if century_number >14: look for last substring
#if century_number is between 11 and 13: match exception
#else: match ends_with

import math
 
def century(year):
    century_number = math.ceil(year / 100)
    if f'{century_number}'.endswith(('11', '12', '13')):
        return f'{century_number}th'
    else:
        ends_with = f'{century_number}'[-1]
        match ends_with:
            case '1':
                return f'{century_number}st'
            case '2':
                return f'{century_number}nd'
            case '3':
                return f'{century_number}rd'
            case _:
                return f'{century_number}th'
        
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True