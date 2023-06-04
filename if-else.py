#Refund Policy Helper

purchased = int(input('How many days ago have you purchased the item? '))
if purchased <= 10:
    print('You can get a refund.')
else:
    print('You cannot get a refund.')

used = input('Have you used the item at all [y/n]? ')
if used == 'n':
    print('You can get a refund.')
else:
    print('You cannot get a refund.')

broken = input('Has the item broken down on its own [y/n]? ')
if broken == 'y':
    print('You can get a refund')
else:
    print('You cannot get a refund')