#write a function, 1 argument (any year greater than 0):to detemine if it's
#a leap year
# if the year is  < 1752: Julian ;leap year(every four year)
# if not: Gregorian; leap year(if the year is divisible by 400 or divisible by 
# 4 but not by 100), return True
# (year is divisible by 100but not by 400) or all other years:
#  return False


def is_leap_year(year):
    if year < 1752:
        if year % 4 == 0:
            return True
        return False
    else:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return year % 4 == 0
    
# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)