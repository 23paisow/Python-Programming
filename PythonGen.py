import random

chars = 'abcdefghijklmnopqrstuvwqyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()~`''"'

number = int(input('How many passwords? - '))

length = int(input('How long do you want your passwords? - '))

while True:
    try:
        websites = str(input('Enter a website name(s): '))
        capss = str(input("Include Capitals and Symbols to your website(s) name: "))
    except:
        print('ERROR')
        continue
    else:
        break

for p in range(number):
    password = ""
    for c in range(length):
                password += random.choice(f"{websites}{capss}")
    print(password)
