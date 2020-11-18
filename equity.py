import math

chanceOfDoubles = 1/6
chanceOfRegRoll = 1 - chanceOfDoubles
movesPerTurn = 2

winReward = 1
lossReward = -1

numPiecesOnLastFile = 4
defaultState = {"blue": numPiecesOnLastFile, "white": numPiecesOnLastFile}

maxTurns = math.ceil(numPiecesOnLastFile / movesPerTurn)

class Turn:
    toPlay = "blue"
    state = defaultState

    def __init__(self, toPlay, state):
        self.toPlay = toPlay
        self.state = state

def evaluateTurnEquity(turn):
    chanceOfWin = 0
    if(turn.toPlay == "blue"):
        if (turn.state["blue"] - movesPerTurn * 2) <= 0:
            chanceOfWin += chanceOfDoubles * winReward
        else:
            chanceOfWin += chanceOfDoubles * evaluateTurnEquity(Turn("white", {"blue": turn.state["blue"] - movesPerTurn * 2, "white": turn.state["white"]}))
        if (turn.state["blue"] - movesPerTurn) <= 0:
            chanceOfWin += chanceOfRegRoll * winReward
        else: 
            chanceOfWin += chanceOfRegRoll * evaluateTurnEquity(Turn("white", {"blue": turn.state["blue"] - movesPerTurn, "white": turn.state["white"]}))
    else:
        if (turn.state["white"] - movesPerTurn * 2) <= 0:
            chanceOfWin += chanceOfDoubles * lossReward
        else: 
            chanceOfWin += chanceOfDoubles * evaluateTurnEquity(Turn("blue", {"blue": turn.state["blue"], "white": turn.state["white"] - movesPerTurn * 2}))
        if (turn.state["white"] - movesPerTurn <= 0):
            chanceOfWin += chanceOfRegRoll * lossReward
        else: 
            chanceOfWin += chanceOfRegRoll * evaluateTurnEquity(Turn("blue", {"blue": turn.state["blue"], "white": turn.state["white"] - movesPerTurn}))
    return chanceOfWin

t = Turn("blue", defaultState)
print("Blue raw equity: ", evaluateTurnEquity(t))           