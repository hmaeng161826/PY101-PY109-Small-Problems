#P
#build a program that RANDOMLY generates & PRINT Teddy's age
#the age should be between 20 and 100, inclusive

#B
#no edge

#C
#when executed, a random number between 20 and 100(inclusive) should be printed
#in sentence 

#A
#1. randomly generates integers
#2. condition is that number is between 20 and 100
#3. print 'Teddy is {random_age} years old!'

name = input('Enter your name: ')

import random
random_age = random.randint(20, 100)
print(f'{name} is {random_age} years old!')


