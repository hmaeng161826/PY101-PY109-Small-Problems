
def triangle(n):
    number_of_stars = 1

    while number_of_stars < n + 1: 
        stars = ('*' * number_of_stars)
        justified_star = stars.rjust(n)
        
        print(justified_star)
        
        number_of_stars += 1
        
triangle(9)

#2nd attempt

def triangle(height):
    for num in range(1, height + 1):
        spaces = ' ' * (height - num) 
        stars = '*' * num
        print(f'{spaces}{stars}')

triangle(10)
