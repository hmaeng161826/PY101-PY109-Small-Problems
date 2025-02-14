#function(string):
    #return string with non-alphabetic characters replaced by space
#how to remove non-alphabetic character?
#replace with space?
#remove all non-a and insert space?
# iterate by each character and if it's alphabet, add alphabet to string
# if it's not alphabet, add ' ' to string. 
#if previous character was non-alpha, continue

def clean_up(string):
    result = ''
    previous_character = ''
    for character in string:
        if character.isalpha():
            result += character
            previous_character = character
        elif previous_character == ' ':
            continue        
        else:
            result += ' '
            previous_character = ' '
    return result
print(clean_up("---what's my +*& line?"))
# True
