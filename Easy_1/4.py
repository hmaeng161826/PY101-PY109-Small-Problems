#Question: user shuold enter the length and width of a room and the #
#program should print the room's area based on the given length and width. #
#Both in square meters and square feet#

#Algorithm #
# 1. user input length and width, in meters
# 2. take the input data and multiply them.
# 3. print the area in meters
# 4. print the area in feet. 10.7639 square feet is 1 square meet. Thus, #
# multiply the outcome in meters by 10. 7639 and print.

length_in_meters = int(input("What's the length of a room in meters?"))
width_in_meters = int(input("What's the width of a room in meters?"))
area_in_meters = length_in_meters * width_in_meters
area_in_feet = area_in_meters *  10.7639

print(f'The area of the room in meters is {area_in_meters} square meters')
print(f'The area of the room in square feet is {area_in_feet} square feet')

#2nd attempt#

length_in_meters = float(input("What's the length of a room in meters? "))
width_in_meters = float(input("What's the width of a room in meters? "))
area_in_meters = length_in_meters * width_in_meters
area_in_feet = area_in_meters *  10.7639

print(f'The area of the room in meters is {area_in_meters:.2f} square meters')
print(f'The area of the room in square feet is {area_in_feet:.2f} square feet')

# Further Exploration #
#1. input to  choose meters or feet
#2. input the dimensions
#3. if 1. is meters, then print area_in_meters
#4. if 1. is feet, then print area_in_feet

measurement_type = input("Enter the measurement type (meters or feet): ")
length = float(input("Enter the length of the room: :"))
width = float(input("Enter the width of the room: "))
area_in_meters = length * width
area_in_feet = area_in_meters * 10.7639
if measurement_type == 'meters':
    area_in_meters = length * width
    area_in_feet = area_in_meters * 10.7639
    print(f'The area of the room is {area_in_meters:.2f} square meter.'
          f'({area_in_feet:.2f} square feet)')
elif measurement_type == 'feet':
    area_in_feet = length * width
    area_in_meters = area_in_feet / 10.7639
    print(f'The area of the room is {area_in_feet:.2f} square feet.'
          f'({area_in_meters:.2f} square meters)')
else: 
    print('Incorrect input')

