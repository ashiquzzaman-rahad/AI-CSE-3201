import random

action: list = []
numOfMoves: list = []
dirtInLocation: list = []
cleanLocation: list = []
    

def randomDirtOnTiles() -> list:
    tiles: list = []
    tiles.append(random.choice([0,1]))
    tiles.append(random.choice([0,1]))
    return tiles


def randomPos() -> int:
    return random.choice([0,1])


def move_right(pos: int) -> int:
    if pos == 0:
        print("moves right...")
        action.append(1)
        numOfMoves.append(1)
        return (pos + 1)
    else:
        print("Blocked...")


def move_left(pos: int) -> int:
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

def total_action_count() -> None:
    global action
    totalAction: int = 0
    for a in action:
        totalAction += a

    print(f"Total actions = {totalAction}")



def total_dirty_location() -> None:
    global dirtInLocation
    totalDirtyLoc: int = 0
    for d in dirtInLocation:
        totalDirtyLoc += d

    print(f"Total dirty locations = {totalDirtyLoc}")



def total_clean_location() -> None:
    global cleanLocation
    totalCleanLoc: int = 0
    for c in cleanLocation:
        totalCleanLoc += c

    print(f"Total clean locations = {totalCleanLoc}")



def total_moves() -> None:
    global numOfMoves
    totalMoves: int = 0
    for m in numOfMoves:
        totalMoves += m

    print(f"Total moves = {totalMoves}")



# def performance_check() ->None:
#     performance: int = 0    
#     performance = totalAction / totalDirtyLoc
#     print(f"Performance: {performance}")




def main():  
    numOfTiles:int = 2
    tiles: list = randomDirtOnTiles()
    timeSteps: int = 1000
    turn: int = 1
    
    pos: int = randomPos()
    for step in range(timeSteps):
        for i in range(numOfTiles):
            if pos == 0:
                suck_dirt(tiles, pos, 'A')
                if turn < numOfTiles:
                    pos = move_right(pos)
                else:
                    pos = move_left(pos)
            else:
                suck_dirt(tiles, pos, 'B')
                if turn < numOfTiles:
                    pos = move_left(pos)
                else:
                    pos = move_right(pos)
            turn += 1
        pos = randomPos()
        tiles = []
        tiles = randomDirtOnTiles()
        turn = 1

    print("Cleaning Completed......!")


main()


