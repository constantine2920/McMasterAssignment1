import PlayerState as Player

import random


Verbs = {
  1: "Smashes",
  2: "Covers",
  3: "Cut",
  4: "Wrecks",
  5: "Vulcan Death Grips"
}

GameChoice = {
  1: "Rock",
  2: "Paper",
  3: "Scissors",
  4: "Lizard",
  5: "Spock"
}

class Spock:
    winner = 0
    winnersName = ""
    winningChoice = 0
    Player1 = 0
    Player2 = 0
    GameNumber = 0
    loosingChoice = 0
    ActionWord = ""
    def __init__(self,gamenumber):
        self.winner = 0
        self.GameNumber = gamenumber
    def ExportDataFromGame(self):
        return self.winner,self.winnersName, self.winningChoice , self.Player1.PlayerName,self.Player1.CurrentState,self.Player2.PlayerName,self.Player2.CurrentState,self.GameNumber

    def PrintSelectionMenu():
        print(F'Select 1 for Rock')
        print(F'Select 2 for Paper')
        print(F'Select 3 for Scissors')
        print(F'Select 4 for Lizard')
        print(F'Select 5 for Spock\n')
    def GenerateVerb(winningChoice, LosingChoice):
        print(f)
    def OutputWinner(self):
        
        if self.winner == 1:
             print(F'\n{self.Player1.PlayerName} was the winner! {GameChoice[self.Player1.CurrentState]} {Verbs[self.Player1.CurrentState]} {GameChoice[self.Player2.CurrentState]}\n')
             self.winnersName = self.Player1.PlayerName
             self.winningChoice = self.Player1.CurrentState
             self.loosingChoice = self.Player2.CurrentState
        elif self.winner == 2:
            print(F'\n{self.Player2.PlayerName} was the winner {GameChoice[self.Player2.CurrentState]} {Verbs[self.Player2.CurrentState]} {GameChoice[self.Player1.CurrentState]}!\n')
            self.winnersName = self.Player2.PlayerName
            self.winningChoice = self.Player2.CurrentState
            self.loosingChoice = self.Player1.CurrentState
        elif self.winner == 3:
            print("\nThe Game was a Draw Replay\n")
            self.winnersName = "Draw"

  
    def GetPlayerDataAutomated(self):
        self.Player1 = Player.PlayerState(1,"Sheldon")
        self.Player2 = Player.PlayerState(2,"Penny")
    def PlayGameFullAuto(self):  
        

        self.GetPlayerDataAutomated()
        #random.randint(1,5)
        self.Player1.SetCurrentState(random.randint(1,5))
        self.Player2.SetCurrentState(random.randint(1,5))
        
        self.WinConditionCheck(self.Player1,self.Player2)
        self.OutputWinner()
        #
    def PlayOneGame(self):
        self.GetPlayerDataAutomated()
        self.WinConditionCheck(self.Player1,self.Player2)
        self.OutputWinner()
    def WinConditionCheck(self ,PlayerState1,PlayerState2):
        
        self.Player1.printStateName()
        self.Player2.printStateName()


        if (PlayerState1.CurrentState == PlayerState2.CurrentState):
            self.winner = 3
        elif PlayerState1.CurrentState == Player.ROCK:
            self.CheckRock()
        elif PlayerState1.CurrentState == Player.PAPER:
            self.CheckPaper()
        elif PlayerState1.CurrentState == Player.SCISSORS:
            self.CheckScissors()
        elif PlayerState1.CurrentState == Player.LIZARD:
            self.CheckLizard()
        elif PlayerState1.CurrentState == Player.SPOCK:
            self.CheckSpock()
        
#The following methods work because we dont need to check for equality anymore Just Win And Loss
    def CheckRock(self):
        if self.Player2.CurrentState == Player.SCISSORS or self.Player2.CurrentState == Player.LIZARD:
            self.winner = 1
        else:
            self.winner = 2
    def CheckPaper(self):
        if self.Player2.CurrentState == Player.SPOCK or self.Player2.CurrentState == Player.ROCK:
            self.winner = 1
        else:
            self.winner = 2    
    def CheckScissors(self):
        if self.Player2.CurrentState == Player.PAPER or self.Player2.CurrentState == Player.LIZARD:
            self.winner = 1
        else:
            self.winner = 2
    def CheckLizard(self):  
        if  self.Player2.CurrentState== Player.SPOCK or self.Player2.CurrentState == Player.PAPER:
            self.winner = 1
        else:
            self.winner = 2
    def CheckSpock(self):
        if self.Player2.CurrentState == Player.ROCK or self.Player2.CurrentState == Player.SCISSORS:
            self.winner = 1
        else:
            self.winner = 2

LenordNemoy = Spock(1)
LenordNemoy.PlayGameFullAuto()

output = LenordNemoy.ExportDataFromGame()


# print(output[0])
# print(output[1])
# print(output[2])
# print(output[3])
