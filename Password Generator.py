import random

print('This is the Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$&^%*(&_+:;'.,/012345647890'

number = input('No of passwords u want to generate: ')
number = int(number)

length = input('Required Password Length: ')
length = int(length)

print('\The Passwords u can choose from: ')

for paswrd in range(number)
  passwords = ' '
    For c in range(length)
     passwords += random.choice(chars)
    print(passwords)

Print("Thank You!")
