#ask the user to enter an integer greater than 0 
#ask the user to enter "s" to compute the sume or "p" to compute the product
#if input is "s": compute the sum between 1 and entered number, inclusive.
#sum = iterate the numbers in range and add 
#if input if "p": compute the product by multiplying all numbers between
#1 and the entered number, inclusive
#product = iterate the numbers in range and multiply the product variable
# print the outcome

number_of_choice = int(input("Please enter an integer greater than 0. "))
outcome_type = input('Enter "s" to compute the sume, or "p" to compute the'
                     'product. ')

if outcome_type == "s":
    summed_number = 0
    for number in range(1, (number_of_choice + 1)):
        summed_number = summed_number + number 
    print(f'The sum of the integers between 1 and {number_of_choice} is '
          f'{summed_number}')

elif outcome_type == "p":
    product_numbers = 1
    for number in range(1, (number_of_choice + 1)):
        product_numbers = product_numbers * number
    print(f'The product of the integers betwwen 1 and {number_of_choice} is '
          f'{product_numbers}.')
else:
    print('Incorrect Input: please enter either "s" or "p".')


