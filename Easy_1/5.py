#propmt for a bill amount
#prompt for a tip rate
#computer the tip. bill amount * tip rate
# compute the total amount: bill amount + tip amount
#print tip amount
# print total amount

bill_amount = float(input('What is the bill? '))
tip_rate = float(input('What is the tip percentage? '))
tip_amount = bill_amount * (tip_rate / 100.0)
total_amount = bill_amount + tip_amount

print(f'The tip is ${tip_amount}')
print(f'The total is ${total_amount}')
