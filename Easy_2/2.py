#ask for user's name: input('Waht is your name? ')
#if input has '!', print HELLO {name}! WHY ARE WE YELLING?
#else: print Hello {name}

name = input('What is your name? ')

if '!' in name:
    print(f'HELLO {name.upper()}! WHY ARE WE YELLING?')
else:
    print(f'Hello {name}.')

