import random

number = random.randint(0,100)
counter = 0

while number != 52:
    number = random.randint(0,100)
    counter = counter + 1
    
    print(counter, number)
    
    ###############
    
    for i in range(10):
        print(i + 2)
    