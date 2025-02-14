# Ask (What is your age?). input will be assigned to a variable 'age'
#Ask (At waht age would you like to retire?) , assign to 'retire_age'
#print current year. 
#remaining years = retire_age - current age
# print 'You will retire in (current year + remaining years
#print 'You have only remaining years years of work to go!

import datetime
current_age = int(input('What is your age? '))
retire_age = int(input('At what age would you like to retire? '))
remaining_years = retire_age - current_age
current_year = datetime.datetime.now().year
print(
    f"It's {current_year}. You will retire "
    f"in {current_year + remaining_years}.\n"
    f"You have only {remaining_years} years of work to go!"
    )

