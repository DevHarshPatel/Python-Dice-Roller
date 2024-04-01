import random
print('--------Welcome to the Dice Roller--------')
flag = True

while True:
    diceRoll = int(input('How many dice would YOU like to ROLL? '))
    for i in range(diceRoll):
        roll = random.randint(1,6)
        if roll == 1:
            print('''
 ____________
|            |
|            |
|     ()     |
|            |
|____________|
            ''')
        elif roll == 2:
            print('''
 ____________
|            |
|            |
|  ()    ()  |
|            |
|____________|''')
        elif roll == 3:
            print('''
 ____________
|            |
|     ()     |
|            |
|  ()    ()  |
|____________|''')
        elif roll == 4:
            print('''
 ____________
|            |
|  ()    ()  |
|            |
|  ()    ()  |
|____________|''')
        elif roll == 5:
            print('''
 ____________
|            |
|  ()    ()  |
|     ()     |
|  ()    ()  |
|____________|''')
        else:
            print('''
 ____________
|            |
|  ()    ()  |
|  ()    ()  |
|  ()    ()  |
|____________|''')
    choice = input('Do you want to PLAY AGAIN (Y or N) ')
    if choice == 'Y' or choice == 'y':
        continue
    else:
        print('--------Thank You for Playing--------')
        print('''
            (((((())))))
          (.'          '.)
         (:              :)
        ((|  () |U| ()   |))   
        ((| ,          , |))
          \  '-......-'  /
           '.          .'
             '-......-''')
        print('----------------END------------------')
        break
    


