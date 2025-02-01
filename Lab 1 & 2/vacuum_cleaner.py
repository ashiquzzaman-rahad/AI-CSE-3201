import random

def randomDirtOnTiles() -> list:
    tiles: list = []
    tiles.append(random.choice([0,1]))
    tiles.append(random.choice([0,1]))
    return tiles


def randomPos() -> int:
    return random.choice([0,1])


def move_right(pos: int, action: list, numOfMoves: list) -> int:
    if pos == 0:
        print("moves right...")
        action.append(1)
        numOfMoves.append(1)
        return (pos + 1)
    else:
        print("Blocked...")


def move_left(pos: int, action: list, numOfMoves: list) -> int:
    if pos == 1:
        print("moves left...")
        action.append(1)
        numOfMoves.append(1)
        return (pos - 1)
    else:
        print("Blocked...")


def suck_dirt(tiles: list, pos: int, tile: str) -> None:  
    if tiles[pos] == 1:
        print(tile,',dirty...')
        dirtInLocation.append(1)
        action.append(1)
        tiles[pos] = 0
        print("sucks dirt...")
    else:
        print(tile,',clean...')
        cleanLocation.append(1)

#main program  


numOfTiles:int = 2
tiles: list = randomDirtOnTiles()
pos: int = randomPos()
turn: int = 1
done: int = 0
timeSteps: int = 1000
action: list = []
numOfMoves: list = []
dirtInLocation: list = []
cleanLocation: list = []

for step in range(timeSteps):
    for i in range(numOfTiles):
        if pos == 0:
            suck_dirt(tiles, pos, 'A')
            if turn < numOfTiles:
                pos = move_right(pos, action, numOfMoves)
            else:
                pos = move_left(pos, action, numOfMoves)
        else:
            suck_dirt(tiles, pos, 'B')
            if turn < numOfTiles:
                pos = move_left(pos, action, numOfMoves)
            else:
                pos = move_right(pos, action, numOfMoves)
        turn += 1
    pos = randomPos()
    tiles = []
    tiles = randomDirtOnTiles()
    turn = 1
    

print("Cleaning Completed......!")

totalAction: int = 0
for a in action:
    totalAction += a

print(f"Total actions = {totalAction}")

totalDirtyLoc: int = 0
for d in dirtInLocation:
    totalDirtyLoc += d

print(f"Total dirty locations = {totalDirtyLoc}")

totalCleanLoc: int = 0
for c in cleanLocation:
    totalCleanLoc += c

print(f"Total clean locations = {totalCleanLoc}")


totalMoves: int = 0
for m in numOfMoves:
    totalMoves += m

print(f"Total moves = {totalMoves}")



performance: int = 0    
performance = totalAction / totalDirtyLoc
print(f"Performance: {performance}")