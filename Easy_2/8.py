#function (list):
#RETURNS every other element of a list (values that are in the 1st,3rd, 5th..)
#a LIST should be returned containing those numbers
#specific indexed elements should be added to the list to create one list
def oddities(lst):
    index = 0
    odd_index = []
    while index < len(lst):
        odd_index.append(lst[index])
        index += 2
    return odd_index

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

#2nd attempt-different approach
def oddities(lst):
    new_list = []
    for idx in range(len(lst)):
        if idx % 2 == 0:
            new_list.append(lst[idx])
    return new_list

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

#Bonus question
def oddities(lst):
    return lst[0::2]
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True