# function(list, dictionary):
# list will contain 2 or more elements that will produce a person's name
# when joined with spaces. 
#ex) ['John' 'Doe'] -> 'John Doe'
# dictionary will contain two keys, "title" and "occupation" and its values
# when function is called, it should RETRUN a GREETING that uses the person's
#FULL NAME(list concatenated) and the person's TITLE (dictionary key)

def greetings(list_names, dictionary_info):
    full_name = ' '.join(list_names)
    title = dictionary_info['title']
    occupation = dictionary_info['occupation']
    greeting = f'Hello, {full_name}! Nice to have a {title} of {occupation}'
    f'around.'
    return greeting

print(greetings(["John", "Q", "Doe"], {"title": "Master", "occupation": "Plumber"}))


#2nd attempt
def greetings(list_names, dictionary_info):
    full_name = ' '.join(list_names)
    title = dictionary_info['title']
    occupation = dictionary_info['occupation']
    return f'Hello, {full_name}! Nice to have a {title} {occupation} around.'

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)

print(greeting)
