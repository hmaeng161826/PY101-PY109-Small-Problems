# string as an argument
#use ord('string') to determine the UTF-16 of the character and compute
#the sum of them.  'string' 

def utf16_value(string):
    summed_code = 0
    for character in string:
        summed_code += ord(character)
    return summed_code

def utf16_value_2(string):
    return sum(ord(character))


# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)