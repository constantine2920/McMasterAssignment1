
ROCK = 1
PAPER = 2
SCISSORS = 3
LIZARD = 4
SPOCK = 5

class PlayerState:
    STARTUP = 0
    ERROR = 6
    CurrentState= 0
    PlayerNumber = 0
    PlayerName = ""
    def __init__(self, playernumber, playername):
        self.PlayerNumber = playernumber
        self.CurrentState = 0
        self.PlayerName = playername
    def SetCurrentState(self, x):
        if x <= 5 or x >= 0: 
            self.CurrentState = x
        else:
            self.CurrentState = self.ERROR
    def printStateName(self):
        if self.CurrentState ==ROCK:
            print(f'({self.CurrentState}) Rock was Selected by Player {self.PlayerName}')
        if self.CurrentState ==PAPER:
            print(f'({self.CurrentState}) Paper was Selected by Player {self.PlayerName}')
        if self.CurrentState ==SCISSORS:
            print(f'({self.CurrentState}) Scissors was Selected by Player {self.PlayerName}')
        if self.CurrentState ==LIZARD:
            print(f'({self.CurrentState}) Lizard was Selected by Player {self.PlayerName}')
        if self.CurrentState ==SPOCK:
            print(f'({self.CurrentState}) Spock was Selected by Player {self.PlayerName}')
  

    

