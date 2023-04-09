import random
import string
import re
import time

while True:
    # generate a string of 25 random characters, doesn't matter what kind of characters
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=25))

    # divide the string into 4 groups akin to a validation key
    group1 = random_string[:6]
    group2 = random_string[6:12]
    group3 = random_string[12:18]
    group4 = random_string[18:]

    # use "-" to deivide them nicely
    final_string = '-'.join([group1, group2, group3, group4])
    print("Randomly generated string:", final_string)

    # define the pattern that will be used
    pattern = r'^[A-Za-z0-9]{6}-[A-Za-z0-9]{6}-[A-Za-z0-9]{6}-[A-Za-z0-9]{7}$'

    # check if the string is valid or not, should always be valid tho
    if re.match(pattern, final_string):
        print("The string is valid.")
    else:
        print("The string is not valid.")

    # wait for 5 seconds before repeating the loop
    time.sleep(5)