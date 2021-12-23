import random

class GuessTheNumber:
    def __init__(self,min,max,yNum,rNUm,guess,guesses,pCh):
        self.yNum = yNum
        self.min = min
        self.max = max
        self.rNum = 0
        self.guess = None
        self.guesses = 1
        self.pCh = None

    def preset(self):
        print('Please select a range:\n1 => 0 - 10\n2 => 0 - 25\n3 => 0 - 50\n4 => 0 - 100\n5 => 0 - 200\n6 => 0 - 250\n7 => 0 - 500\n8 => 0 - 750\n9 0 - 1000\n10 0 - 2000')
        self.pCh = int(input('Type 1 - 10,corresponding to each range -- '))
        if self.pCh == 1:
            print('Guess the number 0 - 10')
            self.min = 0
            self.max = 10
        elif self.pCh == 2:
            print('Guess the number 0 - 25')
            self.min = 0
            self.max = 25
        elif self.pCh == 3:
            print('Guess the number 0 - 50')
            self.min = 0
            self.max = 50
        elif self.pCh == 4:
            print('Guess the number 0 - 100')
            self.min = 0
            self.max = 100
        elif self.pCh == 5:
            print('Guess the number 0 - 200')
            self.min = 0
            self.max = 200
        elif self.pCh == 6:
            print('Guess the number 0 - 250')
            self.min = 0
            self.max = 250
        elif self.pCh == 7:
            print('Guess the number 0 - 500')
            self.min = 0
            self.max = 500
        elif self.pCh == 8:
            print('Guess the number 0 - 750')
            self.min = 0
            self.max = 750
        elif self.pCh == 9:
            print('Guess the number 0 - 1000')
            self.min = 0
            self.max = 1000
        elif self.pCh == 10:
            print('Guess the number 0 - 2000')
            self.min = 0
            self.max = 2000
        while self.pCh > 10:
            print('Please enter a valid value,1 - 10')
            return self.presetOver10()
    
    def presetOver10(self):
        self.pCh = int(input('Type 1 - 10,corresponding to each range -- '))
        if self.pCh == 1:
            print('Guess the number 0 - 10')
            self.min = 0
            self.max = 10
        elif self.pCh == 2:
            print('Guess the number 0 - 25')
            self.min = 0
            self.max = 25
        elif self.pCh == 3:
            print('Guess the number 0 - 50')
            self.min = 0
            self.max = 50
        elif self.pCh == 4:
            print('Guess the number 0 - 100')
            self.min = 0
            self.max = 100
        elif self.pCh == 5:
            print('Guess the number 0 - 200')
            self.min = 0
            self.max = 200
        elif self.pCh == 6:
            print('Guess the number 0 - 250')
            self.min = 0
            self.max = 250
        elif self.pCh == 7:
            print('Guess the number 0 - 500')
            self.min = 0
            self.max = 500
        elif self.pCh == 8:
            print('Guess the number 0 - 750')
            self.min = 0
            self.max = 750
        elif self.pCh == 9:
            print('Guess the number 0 - 1000')
            self.min = 0
            self.max = 1000
        elif self.pCh == 10:
            print('Guess the number 0 - 2000')
            self.min = 0
            self.max = 2000
        while self.pCh > 10:
            print('Please enter a valid value,1 - 10')
            return self.presetOver10()

    def manual(self):
        self.min = int(input('Insert minimum value here: '))
        self.max = int(input('Insert maximum value here: '))
        while self.min >= self.max:
            print('The minimum value has to be lower than the maximum value.')
            return self.manual()        

    def yourGuess(self):
        while True:
            self.guess = int(input('Take a guess here --- '))
            try:
                None
            except:
                continue

            if self.guess < self.rNum:
                print(f'{self.guess} is LOWER than the number.')
            elif self.guess > self.rNum:
                print(f'{self.guess} is HIGHER than the number.')
            else:
                break
            self.guesses += 1

        if self.guesses == 1:
            print(f'It took you {self.guesses} guess to succsesfully guess the number')
        else:
            print(f'It took you {self.guesses} guesses to succsesfully guess the number')
            
    def randomInRangeManual(self):
        self.manual()
        self.rNum = random.randint(self.min,self.max+1)
        self.yourGuess()

    def randomInRnagePreset(self):
        self.preset()
        self.rNum = random.randint(self.min,self.max+1)
        self.yourGuess()

    def play(self): 
        while True:
            print('Choose to manually set range,or use preset by typing "manual" or "preset".')
            choice = str(input('Type here: ')).lower()
            manual_Set = 'manual' 
            manual_Set2 = 'manually'
            preset_Set = 'preset'
            if choice == manual_Set or choice == manual_Set2:
                print('Choose your range: min and max')
                self.randomInRangeManual()
                break
            elif choice == preset_Set:
                self.randomInRnagePreset()      
                break
            else:
                print('Please enter a valid value.')

game = GuessTheNumber(0,0,0,0,0,0,0)
game.play()