#write a function(non-empty string):
    #RETURNS the middle character of the string.
    #middle character: index of the character is half point of the total length
    #if the string has an even length (len(string) % 2 = 0), return characters
    #EX) odd length: abcdefg; total length = 7; (7 // 2) + (7 % 2)
    #    even length: abcdef; total length = 6; (6 // 2), (6 // 2) + 1

def center_of(str):
    if len(str) % 2 == 0:
        return str[(len(str) // 2) - 1] + str[(len(str) // 2)]
    else:
        return str[(len(str) // 2) - 1]
print(center_of('I Love Python!!!'))
print(center_of('Launch School'))      
print(center_of('Launchschool'))    
print(center_of('Launch'))          
print(center_of('Launch School is #1')) 
print(center_of('x'))
print(len('I Love Python!!!'))

    
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True