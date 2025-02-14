#function(text):
 #print in a box (use new line,

def print_in_box(text):
    print('+' +  ('-' * (len(text) + 2)) + '+')
    print('|' + (' ' * (len(text) + 2)) + '|')
    print('|' + ' ' + text + ' ' + '|')
    print('|' + (' ' * (len(text) + 2)) + '|')
    print('+' +  ('-' * (len(text) + 2)) + '+')

print_in_box('To boldly go where no one has gone before.')

print_in_box('')

#2nd attempt

def print_in_box(text):
    text_length = len(text)
    horizontal_rule = '+' +  '-' * (text_length + 2) + '+'
    empty_rule = '|' + ' ' * (text_length + 2) + '|'

    print(horizontal_rule)
    print(empty_rule)
    print(f'| {text} |')
    print(empty_rule)
    print(horizontal_rule)

print_in_box('To boldly go where no one has gone before.')

print_in_box('')

#further exploration

def print_in_box(text, max_width):
    available_width = max_width - 2
    text_length = len(text)
    max_horizontal = '+' + '-' * available_width + '+'
    max_empty = '|' + ' ' * available_width + '|'
    horizontal_rule = '+' +  '-' * (text_length + 2) + '+'
    empty_rule = '|' + ' ' * (text_length + 2) + '|'
    
    if text_length >= max_width:
        print(max_horizontal)
        print(max_empty)
        print(f'| {text[ : available_width - 2]} |')
        print(max_empty)
        print(max_horizontal)

    else:
        print(horizontal_rule)
        print(empty_rule)
        print(f'| {text} |')
        print(empty_rule)
        print(horizontal_rule)

print_in_box('To boldly go where no one has gone before.', 13)

