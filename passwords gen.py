import string
import secrets

# how long it is (:flushed:)
length = 16

# what to use for password
characters = string.ascii_letters + string.digits + string.punctuation

# generate shit
password = ''.join(secrets.choice(characters) for i in range(length))

# show the password
print(password)

# this shit is too long idk if someone would remember such passwords LMAO