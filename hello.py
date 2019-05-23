import random
# This is a simple rock paper scissors I made to learn/practice python

def compChoose():
    return random.randint(1,3)

def playerChoose():
    print("press 1 for rock, 2 for paper, or 3 for scissors")
    playerChoice = int(input())
    if(playerChoice < 4):
        return playerChoice

def decide(compChoose, playerChoose):
            if(playerChoose == compChoose):
                  print("It's a tie")
            else:
                print("Computer chose: " + str(compChoose))
                if(compChoose == 1):
                     if(playerChoose == 3):
                         print("you win")
                     else: print("you lose")

                if(compChoose == 2):
                     if(playerChoose == 1):
                         print("you win")
                     else: print("you lose")

                if(compChoose == 3):
                     if(playerChoose == 2):
                         print("you win")
                     else: print("you lose")
            return()
def main():
              decide(compChoose(), playerChoose())

if __name__ == "__main__":
    main()

