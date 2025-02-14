# function(string):
    #return a new string with duplicated characters collapsed into a single
    #character; 

def crunch(text):

    if text == '':
        return ''

    previous_character = text[0]
    crunched = text[0]

    for character in text[1:]:
        if character != previous_character:
            crunched += character
            previous_character = character
    return crunched


# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
