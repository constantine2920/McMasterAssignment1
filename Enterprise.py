import Spock as Voyage
import PlayerState as Player

OUTPUTGAMES = 1
GAMESTORUN = 1000

GamesTakenToReachAllPossibleOutcomes = 0


CurrentGameCount = 1

GameChoice = {
  1: "Rock",
  2: "Paper",
  3: "Scissors",
  4: "Lizard",
  5: "Spock"
}

PlayersThatChooseRock = 0
PlayersThatChoosePaper = 0
PlayersThatChooseScissors = 0
PlayersThatChooseLizard = 0
PlayersThatChooseSpock = 0

AllGames = []

GamesWithARockWinner = []
GamesWithAPaperWinner = []
GamesWithAScissorsWinner = []
GamesWithALizardWinner = []
GamesWithASpockWinner = []

GamesWithTies = []

GamesPlayerOneWon = []
GamesPlayerTwoWon = []
def OutputAndStoreGameList(Games):
    print(F'{len(Games)} Games in the Set')
def OutputCluster(GamesWithAWinner,ClusterName,verbose):
    print(f"Games Catagory: {ClusterName}")
    print(F'{len(GamesWithAWinner)} Games in the Cluster Percent  { (len(GamesWithAWinner) / len(AllGames))*100 }%')
    print(F'Game#  Winner P1 P2 \n'  )
    if verbose ==1:
        for Games in GamesWithAWinner:
            print(f'{Games.GameNumber}  {Games.winningChoice} {Games.Player1.CurrentState} {Games.Player2.CurrentState} ')
def outputGame(missionResults):
    print("Winner's Name: ", missionResults[1])
    if missionResults[0] < 3:
        print("Game Winning Player ", missionResults[0])
    else:
        print("Game was a draw StateCode: ", missionResults[0])
    print("WinningChoice Choice: ", missionResults[2])
    print("Player 1's Name: ",missionResults[3])
    print("Player 1 selected: ", GameChoice[missionResults[4]])
    print("Player 2's Name: ", missionResults[5])
    print("Player 2 selected: ", GameChoice[missionResults[6]])
    print("Game Number ", missionResults[7], "\n")
def ClassifyResults(missionResults,mission):
    AllGames.append(mission)
    
    if missionResults[0] == 3:
        GamesWithTies.append(mission)
    elif missionResults[0] == 1:
        GamesPlayerOneWon.append(mission)
    elif missionResults[0] == 2:
        GamesPlayerTwoWon.append(mission)
    if missionResults[2]== Player.ROCK:
        GamesWithARockWinner.append(mission)
    elif missionResults[2]== Player.PAPER:
        GamesWithAPaperWinner.append(mission)
    elif missionResults[2]== Player.SCISSORS:
        GamesWithAScissorsWinner.append(mission)
    elif missionResults[2] == Player.LIZARD:
        GamesWithALizardWinner.append(mission)
    elif missionResults[2]== Player.SPOCK:
        GamesWithASpockWinner.append(mission)

    if OUTPUTGAMES==1:
        outputGame(missionResults)
while CurrentGameCount <=GAMESTORUN: 
    EnterpriseMission = Voyage.Spock(CurrentGameCount)
    EnterpriseMission.PlayGameFullAuto()
    CurrentGameCount = CurrentGameCount+1  
    MissionResults = EnterpriseMission.ExportDataFromGame()
    ClassifyResults(MissionResults,EnterpriseMission)

# OutputCluster(GamesPlayerOneWon,"\n Games Sheldon Won ,", OUTPUTGAMES)
# OutputCluster(GamesPlayerTwoWon,"\n Games Penny Won ,", OUTPUTGAMES)

# OutputCluster(GamesWithTies,"\n Games That Ended in a Tie ,", OUTPUTGAMES)


# OutputCluster(GamesWithARockWinner,"\n Games With a Rock Winner,", OUTPUTGAMES)
# OutputCluster(GamesWithAPaperWinner,"\n Games With a Paper Winner,", OUTPUTGAMES)
# OutputCluster(GamesWithAScissorsWinner,"\n Games With a Scissors Winner,", OUTPUTGAMES)
# OutputCluster(GamesWithALizardWinner,"\n Games With a Lizard Winner,", OUTPUTGAMES)
# OutputCluster(GamesWithASpockWinner,"\n Games With a Spock Winner,", OUTPUTGAMES)
