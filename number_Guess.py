import random
guess = int(0)
choice = None
a = 1
    
# def num_Range():
#         print('Choose to manually set range,or use preset by typing "manual" or "preset".')
#         choice = str(input('Type here: ')).lower()
#         manual_Set = 'manual'
#         preset_Set = 'preset'

def preset(min,max):
        print('Ranges: 0-50,0-100,0-200,0-250,0-500,0-750,0-1000')
        preset1 = 1
        preset2 = 2
        preset3 = 3
        preset4 = 4 
        preset5 = 5
        preset6 = 6
        preset7 = 7
        print('Choose from 1 to 7,coresponding to each range') 
        preset_Choose = int(input('Type here: '))
        

def manual():
        min = int(input('Insert minimum value here: '))
        max = int(input('Insert maximum value here: '))
        rNum = random.randint(min,max+1)
        print(rNum)
        while min >= max:
            print('The minimum value has to be lower than the maximum value.')
            return manual()


def randomGuess():
    while True:
        
    




while True:
    print('Choose to manually set range,or use preset by typing "manual" or "preset".')
    choice = str(input('Type here: ')).lower()
    manual_Set = 'manual'
    preset_Set = 'preset'
    if choice == manual_Set:
        print('Choose your range: min and max')
        manual()
        if True:
            None
        break
        
    elif choice == preset_Set:
        print('Choose a range: ')
        
    else:
        print('Please enter a valid value.')
