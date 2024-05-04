import random

text = 'AKVNJVTFB1234567890.,=+_-'
password = " "

for i in range(10):
    password += random.choice(text)

print(password)

