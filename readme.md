# Python Dice Rolling Simulator

This project is ✏️SIMPLE, 🎉FUN, 🥸INTERESTING.

It uses the following PYTHON concepts:

  - Randomising
  
  - While loops
  
  - For loop
  
  - Input
  
  - ASCII art(not particularly a python concept)
  
  - Conditional Statements

## How does it work?

It first ask for the number of rolls of the dice you want .


<kbd>![Screenshot 2024-04-01 123234](https://github.com/DevHarshPatel/Python-Dice-Roller/assets/122734195/bf109b32-d7cb-40a5-adf8-de2841785654)</kbd>



Then it randomises between 1-6 and then prints that dice's ASCII art for the targeted times each time with a random side from 1 - 6.(For this instance our user wants  3 different dice rolls. )


<kbd>![Screenshot 2024-04-01 123613](https://github.com/DevHarshPatel/Python-Dice-Roller/assets/122734195/cdd14f80-0462-41a4-a612-6ef57abc8996)</kbd>


At last it ask for the user's preference to continue the game or not:


<kbd>![Screenshot 2024-04-01 123808](https://github.com/DevHarshPatel/Python-Dice-Roller/assets/122734195/e10e2021-07d4-4be4-a0e5-0d7546892f8b)</kbd>


If the user don't want to continue, it display a Greeting with a Happy face.


<kbd>![Screenshot 2024-04-01 124123](https://github.com/DevHarshPatel/Python-Dice-Roller/assets/122734195/27d6e8fc-bb52-42b9-97d1-c54380bc7362)</kbd>

## CODE

```python
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
    

```

## Some words from me

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣀⢠⡤⠤⠖⠒⠒⠒⠲⣆⠀⠀⠀⠀⣾⠋⠉⠉⠛⢷⠀⣴⠖⠒⠤⣄⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠤⠶⢺⣾⣏⠁⠀⠀⣧⣼⣇⣀⠀⠀⠀⡀⠀⠘⡆⠀⠀⢰⣏⠀⠀⠀⠀⠘⣿⡟⠀⠀⢠⢃⣼⡏⠉⠙⢳⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⡤⠴⠒⠋⠙⣇⣿⠀⠀⠀⣿⣿⠀⠀⠀⢸⣿⣿⣿⠃⠀⢰⣿⡀⠀⠹⡄⠀⢸⣿⠀⠀⠀⠀⠀⢹⡇⠀⠀⢸⡿⣽⠀⠀⠀⡜⠀⣀⡤⠖⠓⠢⢤⣀⠀
⣠⡴⠒⠉⠁⠀⠀⠀⠀⠀⠸⣿⡇⠀⠀⠘⠛⠃⠀⠀⠈⡟⠉⣿⠀⠀⠘⠛⠃⠀⠀⢷⠀⢸⣿⠀⠀⢠⡀⠀⠀⠀⠀⠀⣿⢧⡇⠀⠀⠸⠗⠚⠁⠀⠀⠀⣀⣠⣾⠃
⣿⡇⠀⠀⠀⠀⠀⠀⣶⣶⣿⢿⢹⠀⠀⠀⢀⣀⠀⠀⠀⢳⠀⣿⠀⠀⢀⣀⣤⠀⠀⠘⣇⢸⡏⠀⠀⢸⣧⠀⠀⠀⠀⢸⣿⡿⠀⠀⢀⠀⠀⠀⢀⣤⣶⣿⠿⠛⠁⠀
⢧⣹⣶⣾⣿⡄⠀⠀⠸⡟⠋⠘⡜⡆⠀⠀⢻⣿⡇⠀⠀⢸⡀⣿⠀⠀⢸⣿⡿⡇⠀⠀⢸⣿⡇⠀⠀⢸⡿⡆⠀⠀⠀⣾⣿⠃⠀⠀⣾⡇⠀⠀⠈⡟⠉⠀⠀⠀⠀⠀
⠘⣿⡿⠿⢿⣧⠀⠀⠀⢳⡀⠀⣇⢱⠀⠀⠈⣿⣷⠀⣀⣸⣷⣿⣤⣤⣼⠋⣇⣹⣶⣶⣾⣿⡿⢲⣶⣾⡇⣿⣤⣀⣀⣿⡏⠀⠀⣼⡏⢧⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⡞⣇⠀⠀⠀⢧⠀⢸⣈⣷⣶⣶⣿⣿⣿⣿⣿⣿⣿⣽⣿⡏⢀⡼⠟⠛⠻⢿⡿⠿⠿⣿⣁⣿⣿⣿⣿⣿⣿⣿⣶⣴⢿⠁⢸⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣼⣦⣤⣶⣿⠁⣀⣿⠿⠿⣿⣫⣿⠉⠁⠀⠀⠀⡏⠀⣴⠏⠀⠀⠀⠀⠀⠹⣆⠀⢠⣿⠀⠀⠀⢈⠟⢻⡿⠿⣅⣘⡆⣸⣇⠀⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⠿⠿⠛⠃⢠⣿⣷⣄⠀⠈⠙⠋⠀⠀⠀⠀⣸⢁⡾⠁⠀⠀⣠⣤⡀⠀⠀⠸⣤⡞⡇⠀⠀⠀⢸⣰⣿⠃⠀⠀⢹⣿⣿⣿⣿⣦⣼⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⣿⣾⠇⠀⠀⣸⣿⣿⢿⠀⠀⠀⣿⢁⡇⠀⠀⢀⣿⣿⡏⠀⠀⠀⡼⠀⢙⣿⠛⠻⣏⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⠀⠀⠀⠀⢸⡿⡿⠀⠀⠀⡏⢹⠟⡟⠀⠀⠀⡿⢸⠀⠀⠀⢸⣿⡿⠀⠀⠀⢠⠇⡰⢋⡏⠀⠀⠀⢙⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡿⡿⠀⠀⠀⠀⣸⡇⡇⠀⠀⠀⠻⠾⠞⠁⠀⠀⢀⡇⡏⠀⠀⠀⢸⣿⠃⠀⠀⠀⡼⣰⠃⡞⠀⠀⠀⠀⡾⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⡇⠀⠀⠀⠀⣿⣇⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣃⡇⠀⠀⠀⠀⠀⠀⠀⠀⣼⣷⠃⣼⡀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⠃⠀⠀⠀⢀⡇⢿⣿⣧⣀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣽⣿⣷⣤⡞⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣼⣤⣶⣶⣶⡿⠁⠈⢿⣿⣿⣿⣿⣿⣿⣿⠿⠃⢸⣿⣿⣷⣤⣄⣀⣀⣤⣾⣏⣤⡟⠁⠀⠈⠻⡍⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠿⠿⠿⠟⠛⠁⠀⠀⠀⠉⠛⠛⠛⠛⠉⠁⠀⠀⠀⠙⠿⢿⣿⣿⡿⠿⠋⢀⣿⣿⣧⡀⠀⠀⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

Thank you 😌 for your precious time⌛⌚. I would eagerly be awaiting for your feedback or anything else I could improve.


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀
