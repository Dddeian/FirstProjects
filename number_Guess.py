import random

class GuessTheNumber:
    def __init__(self,min,max,yNum,rNUm,guess,guesses,pCh,number):
        self.yNum = yNum
        self.min = min
        self.max = max
        self.rNum = 0
        self.guess = None
        self.guesses = 1
        self.pCh = None
        self.number = None


    def preset(self):
        print(50*str('*') + '\nPlease select a range:\n1 => 0 - 10\n2 => 0 - 25\n3 => 0 - 50\n4 => 0 - 100\n5 => 0 - 200\n6 => 0 - 250\n7 => 0 - 500\n8 => 0 - 750\n9 => 0 - 1000\n10 => 0 - 2000')
        self.pCh = int(input(50*str('*') + '\nType 1 - 10,corresponding to each range -- '))
        if self.pCh == 1:
            print(50*str('*') + '\nGuess the number 0 - 10\n')
            self.min = 0
            self.max = 10
        elif self.pCh == 2:
            print(50*str('*') + '\nGuess the number 0 - 25\n')
            self.min = 0
            self.max = 25
        elif self.pCh == 3:
            print(50*str('*') + '\nGuess the number 0 - 50\n')
            self.min = 0
            self.max = 50
        elif self.pCh == 4:
            print(50*str('*') + '\nGuess the number 0 - 100\n')
            self.min = 0
            self.max = 100
        elif self.pCh == 5:
            print(50*str('*') + '\nGuess the number 0 - 200\n')
            self.min = 0
            self.max = 200
        elif self.pCh == 6:
            print(50*str('*') + '\nGuess the number 0 - 250\n')
            self.min = 0
            self.max = 250
        elif self.pCh == 7:
            print(50*str('*') + '\nGuess the number 0 - 500\n')
            self.min = 0
            self.max = 500
        elif self.pCh == 8:
            print(50*str('*') + '\nGuess the number 0 - 750\n')
            self.min = 0
            self.max = 750
        elif self.pCh == 9:
            print(50*str('*') + '\nGuess the number 0 - 1000\n')
            self.min = 0
            self.max = 1000
        elif self.pCh == 10:
            print(50*str('*') + '\nGuess the number 0 - 2000\n')
            self.min = 0
            self.max = 2000
        while self.pCh > 10:
            print(50*str('*') + '\nPlease enter a valid value,1 - 10')
            return self.presetOver10()
    

    def yourGuessPreset(self):
        while True:
            self.guess = input('\nTake a guess here --- ')
            try:
                self.guess = int(self.guess)
            except ValueError:
                print(50*str('*') + '\nEnter a NUMBER!')
                return self.yourGuessPreset()
                
            if self.guess < self.rNum:
                print(50*str('*') + f'\n{self.guess} <--- than the number.')
            elif self.guess > self.rNum:
                print(50*str('*') + f'\n{self.guess} ---> than the number.')
            else:
                break
            self.guesses += 1

        if self.pCh == 1:
            if self.guesses == 1:
                print(f'You succesfully guessed the number in {self.guesses} guess.Thats a great score!')
            elif self.guesses < 3:
                print(f'You succsesfully guessed the number in {self.guesses} guesses.Thats a great score!')
            elif self.guesses > 2 and self.guesses < 6:
                print(f'You succesfully guessed the number in {self.guesses} guesses.Thats a good score!')
            elif self.guesses > 5 and self.guesses <  11:
                print(f'You succesfully guessed the number in {self.guesses} guesse.Not a bad score!')
            elif self.guesses > 10:
                print(f'You succssefully guessed the number in {self.guesses} guessses.You can do better!')
        elif self.pCh == 2:
            if self.guesses == 1:
                print(f'You succesfully guessed the number in {self.guesses} guess.Thats a great score!')
            elif self.guesses < 3:
                print(f'You succsesfully guessed the number in {self.guesses} guesses.Thats a great score!')
            elif self.guesses > 2 and self.guesses < 6:
                print(f'You succesfully guessed the number in {self.guesses} guesses.Thats a good score!')
            elif self.guesses > 5 and self.guesses <  11:
                print(f'You succesfully guessed the number in {self.guesses} guesse.Not a bad score!')
            elif self.guesses > 10:
                print(f'You succssefully guessed the number in {self.guesses} guessses.You can do better!')
        elif self.pCh == 3:
            if self.guesses == 1:
                print(f'You succesfully guessed the number in {self.guesses} guess.Thats a great score!')
            elif self.guesses < 4:
                print(f'You succsesfully guessed the number in {self.guesses} guesses.Thats a great score!')
            elif self.guesses > 3 and self.guesses < 9:
                print(f'You succesfully guessed the number in {self.guesses} guesses.Thats a good score!')
            elif self.guesses > 8 and self.guesses <  14:
                print(f'You succesfully guessed the number in {self.guesses} guesse.Not a bad score!')
            elif self.guesses > 13:
                print(f'You succssefully guessed the number in {self.guesses} guessses.You can do better!')
        elif self.pCh == 4:
            if self.guesses == 1:
                print(f'You succesfully guessed the number in {self.guesses} guess.Thats a great score!')
            elif self.guesses < 6:
                print(f'You succsesfully guessed the number in {self.guesses} guesses.Thats a great score!')
            elif self.guesses > 5 and self.guesses < 11:
                print(f'You succesfully guessed the number in {self.guesses} guesses.Thats a good score!')
            elif self.guesses > 10 and self.guesses <  16:
                print(f'You succesfully guessed the number in {self.guesses} guesse.Not a bad score!')
            elif self.guesses > 15:
                print(f'You succssefully guessed the number in {self.guesses} guessses.You can do better!')
        elif self.pCh == 5:
            if self.guesses == 1:
                print(f'You succesfully guessed the number in {self.guesses} guess.Thats a great score!')
            elif self.guesses < 8:
                print(f'You succsesfully guessed the number in {self.guesses} guesses.Thats a great score!')
            elif self.guesses > 7 and self.guesses < 13:
                print(f'You succesfully guessed the number in {self.guesses} guesses.Thats a good score!')
            elif self.guesses > 12 and self.guesses <  18:
                print(f'You succesfully guessed the number in {self.guesses} guesse.Not a bad score!')
            elif self.guesses > 17:
                print(f'You succssefully guessed the number in {self.guesses} guessses.You can do better!')
        elif self.pCh == 6:
            if self.guesses == 1:
                print(f'You succesfully guessed the number in {self.guesses} guess.Thats a great score!')
            elif self.guesses < 9:
                print(f'You succsesfully guessed the number in {self.guesses} guesses.Thats a great score!')
            elif self.guesses < 8 and self.guesses < 14:
                print(f'You succesfully guessed the number in {self.guesses} guesses.Thats a good score!')
            elif self.guesses > 13 and self.guesses <  19:
                print(f'You succesfully guessed the number in {self.guesses} guesse.Not a bad score!')
            elif self.guesses > 18:
                print(f'You succssefully guessed the number in {self.guesses} guessses.You can do better!')
        elif self.pCh == 7:
            if self.guesses == 1:
                print(f'You succesfully guessed the number in {self.guesses} guess.Thats a great score!')
            elif self.guesses < 10:
                print(f'You succsesfully guessed the number in {self.guesses} guesses.Thats a great score!')
            elif self.guesses > 9 and self.guesses < 15:
                print(f'You succesfully guessed the number in {self.guesses} guesses.Thats a good score!')
            elif self.guesses > 14 and self.guesses <  20:
                print(f'You succesfully guessed the number in {self.guesses} guesse.Not a bad score!')
            elif self.guesses > 19:
                print(f'You succssefully guessed the number in {self.guesses} guessses.You can do better!')
        elif self.pCh == 8:
            if self.guesses == 1:
                print(f'You succesfully guessed the number in {self.guesses} guess.Thats a great score!')
            elif self.guesses < 11:
                print(f'You succsesfully guessed the number in {self.guesses} guesses.Thats a great score!')
            elif self.guesses > 10 and self.guesses < 17:
                print(f'You succesfully guessed the number in {self.guesses} guesses.Thats a good score!')
            elif self.guesses > 16 and self.guesses <  22:
                print(f'You succesfully guessed the number in {self.guesses} guesse.Not a bad score!')
            elif self.guesses > 21:
                print(f'You succssefully guessed the number in {self.guesses} guessses.You can do better!')
        elif self.pCh == 9:
            if self.guesses == 1:
                print(f'You succesfully guessed the number in {self.guesses} guess.Thats a great score!')
            elif self.guesses < 12:
                print(f'You succsesfully guessed the number in {self.guesses} guesses.Thats a great score!')
            elif self.guesses > 11 and self.guesses < 18:
                print(f'You succesfully guessed the number in {self.guesses} guesses.Thats a good score!')
            elif self.guesses > 17 and self.guesses <  23:
                print(f'You succesfully guessed the number in {self.guesses} guesse.Not a bad score!')
            elif self.guesses > 22:
                print(f'You succssefully guessed the number in {self.guesses} guessses.You can do better!')
        elif self.pCh == 10:
            if self.guesses == 1:
                print(f'You succesfully guessed the number in {self.guesses} guess.Thats a great score!')
            elif self.guesses < 14:
                print(f'You succsesfully guessed the number in {self.guesses} guesses.Thats a great score!')
            elif self.guesses > 13 and self.guesses < 20:
                print(f'You succesfully guessed the number in {self.guesses} guesses.Thats a good score!')
            elif self.guesses > 19 and self.guesses <  25:
                print(f'You succesfully guessed the number in {self.guesses} guesse.Not a bad score!')
            elif self.guesses > 24:
                print(f'You succssefully guessed the number in {self.guesses} guessses.You can do better')
   
   
    def presetOver10(self):
        self.pCh = int(input(50*str('*') + '\nType 1 - 10,corresponding to each range -- '))
        if self.pCh == 1:
            print(50*str('*') + '\nGuess the number 0 - 10')
            self.min = 0
            self.max = 10
        elif self.pCh == 2:
            print(50*str('*') + '\nGuess the number 0 - 25')
            self.min = 0
            self.max = 25
        elif self.pCh == 3:
            print(50*str('*') + '\nGuess the number 0 - 50')
            self.min = 0
            self.max = 50
        elif self.pCh == 4:
            print(50*str('*') + '\nGuess the number 0 - 100')
            self.min = 0
            self.max = 100
        elif self.pCh == 5:
            print(50*str('*') + '\nGuess the number 0 - 200')
            self.min = 0
            self.max = 200
        elif self.pCh == 6:
            print(50*str('*') + '\nGuess the number 0 - 250')
            self.min = 0
            self.max = 250
        elif self.pCh == 7:
            print(50*str('*') + '\nGuess the number 0 - 500')
            self.min = 0
            self.max = 500
        elif self.pCh == 8:
            print(50*str('*') + '\nGuess the number 0 - 750')
            self.min = 0
            self.max = 750
        elif self.pCh == 9:
            print(50*str('*') + '\nGuess the number 0 - 1000')
            self.min = 0
            self.max = 1000
        elif self.pCh == 10:
            print(50*str('*') + '\nGuess the number 0 - 2000')
            self.min = 0
            self.max = 2000
        while self.pCh > 10:
            print(50*str('*') + '\nPlease enter a valid value,1 - 10')
            return self.presetOver10()


    def manual(self):
        self.min = int(input('Minumum: '))
        self.max = int(input('Maximum: '))
        print(f'Guess a number {self.min}-{self.max}')
        while int(self.min) >= int(self.max):
            print(50*str('*') + '\nThe MINIMUM value has to be LOWER than the MAXIMUM value.')
            return self.manual()    
    

    def yourGuessManual(self):
            while True:
                self.guess = input('\nTake a guess --- ')
                try:
                    self.guess = int(self.guess)
                except ValueError:
                    print(50*str('*') + '\nEnter a NUMBER!')
                    return self.yourGuessManual()
                    
                if self.guess < self.rNum:
                    print(50*str('*') + f'\n{self.guess} <--- than the number.')
                elif self.guess > self.rNum:
                    print(50*str('*') + f'\n{self.guess} ---> than the number.')
                else:
                    break
                self.guesses += 1
    
            if self.guesses == 1:
                print(f'\nCongrats!It took you {self.guesses} guess to succsesfully guess the number.\n' + 50*str('*'))
            else:
                print(f'\nCongrats!It took you {self.guesses} guesses to succsesfully guess the number.\n' + 50*str('*'))
   

    def randomInRangeManual(self):
        self.manual()
        self.rNum = random.randint(self.min,self.max)
        self.yourGuessManual()


    def randomInRnagePreset(self):
        self.preset()
        self.rNum = random.randint(self.min,self.max)
        self.yourGuessPreset()


    def play(self): 
        while True:
            print(50*str('*') + '\nChoose to manually set range,or use preset by typing "manual" or "preset".')
            choice = str(input('Type here: ')).lower()
            manual_Set = 'manual' 
            manual_Set2 = 'manually'
            preset_Set = 'preset'
            if choice == manual_Set or choice == manual_Set2:
                print(50*str('*') + '\nChoose your range: min and max')
                self.randomInRangeManual()
                if self.min == str('stop'):
                    break
                else:
                    print('\nhttps://youtu.be/QcqaQ47ywD0?t=55\n')
                    break
            elif choice == preset_Set:
                self.randomInRnagePreset()  
                print('\nhttps://youtu.be/QcqaQ47ywD0?t=55\n') 
                break
            elif choice == str('stop') or str('break'):
                break
            else:
                print(50*str('*') + '\nPlease enter a valid value.')


game = GuessTheNumber(0,0,0,0,0,0,0,0)
game.play()
