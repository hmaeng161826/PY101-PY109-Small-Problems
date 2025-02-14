#write a function, 1 argument (any year greater than 0):to detemine if it's
#a leap year
# if the year is a leap year(the year is divisible by 400 or divisible by 
# 4 but not by 100), return True
# if not (year is divisible by 100but not by 400) or all other years:
#  return False

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        if year % 100 != 0:
            return True
        return False
    else:
        return False
    
# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == False)
print(is_leap_year(1100) == False)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == False)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)