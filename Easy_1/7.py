#1. function to take two strings(shorter, longer) and return the following:
# shorter string+longer string+ shorter string
#2. The length of both strings should be determined and compared to determine
#which one is shorter and which one is longer
#3. if the length of str1 is shorter than str2: shorter_string = str1
#4. return the result. result: shorter+longer+shorter
#if not: shorter_string = str2

def short_long_short(str1, str2):
    if len(str1) < len(str2):
        return str1 + str2 + str1
    else:
        return str2 + str1 + str2


    # These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")
