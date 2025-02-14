#function(number):
    #returns doubled number: 
    # doubled condition: 1) number is even-length(2, 4, 6) 
    #when divided by 2, left-side = right-side. 
    #ex) 4 digits number = 2222 ; 4 // 2 = 2; '2222'[:(2-1)] = '2222'[2:]
    #if it's doubl number, return as is 
    #scenario: 1) even-length 2) odd-length
    # 1-1) left == right
    # 1-2) left != right
    # 

def twice(number):
    str_num = f'{number}'
    if len(str_num) % 2 == 0:
        middle_point = len(str_num) // 2
        left_side = str_num[:(middle_point)] 
        right_side = str_num[middle_point:]
        if left_side == right_side:
            return number
        return number * 2
    else:
        return number * 2
    
print(twice(37) == 74)                 # True
print(twice(44) == 44)                 # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True

#2nd attempt
def is_double(number):
    str_num = f'{number}'
    middle_point = len(str_num) // 2
    left_side = str_num[:(middle_point)] 
    right_side = str_num[middle_point:]

    return True if left_side == right_side else False    

def twice(number):
    if is_double(number):
        return number
    else:
        return number * 2
    
print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True