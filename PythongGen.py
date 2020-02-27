import random
import string

chars = 'abcdefghijklmnopqrstuvwqyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

number = int(input('How many passwords? - '))

length = int(input('How long do you want your passwords? - '))

while True:
    try:
        websites = str(input('Enter website names(NO SPACES!): '))
        capss = str(input("Put some of your favorite CAPS and symbols(NO SPACES!): "))
        final = str(input(f"{websites}{capss}"))
    except:
        print('ERROR')
        continue
    else:
        break

websites = ""

for p in range(number):
    final = ""
    for c in range(length):
        for w in range(0, len(websites)):
            for a in range(capss):
                    def final():
                        final = final
                        return ''.join(random.choice(final) for f in range(final))
print(final)