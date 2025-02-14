def penultimate(string):
    return string.split(' ')[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

#2nd attempt

def penultimate(string):
    splitted_word = string.split()
    return splitted_word[-2]

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")