import random
import math


def environmenCreate(tiles: list) -> None:
    for i in range(5):
        for j in range(7):
            tiles[i][j] = random.choice([0,1,1])


def randomPosition() -> list:
    a: int = math.floor(random.random() * 3) + 1 #row
    b: int = math.floor(random.random() * 5) + 1 #column
    return [a, b]

def collectObj(tiles: list, row: int, column: int, action: list, collect: list) -> None:
    # print(row, column)
    if tiles[row][column] == 0:
        print(f"tile({row},{column}) doesnot have any object!")
    else:
        print(f"tile({row},{column}) has object! collecting...")
        action.append(1)
        collect.append(1)
        tiles[row][column] = 0

def randomMove(column: int, row: int, action: list, move: list, prev_pos: int) -> list:
    moveChoice: int = math.floor(random.random() * 4)
    while(prev_pos == moveChoice):
        moveChoice = math.floor(random.random() * 4)

    match(moveChoice):
        case 0: #left
            column -= 1
            prev_pos = 2
            print("Move left!")
        case 1: #up
            row -= 1
            prev_pos = 3
            print("Move up!")
        case 2: #right
            column += 1
            prev_pos = 0
            print("Move right!")
        case 3: #down
            row += 1
            prev_pos = 1
            print("Move down!")
        case _: #anrowthing else
            print("invalid!")

    action.append(1)
    move.append(1)
    return [row, column, prev_pos]

def showingMovement(row, column, tiles):
    for i in range(5):
        for j in range(7):
            if(i == row and j == column):
                print("|_|", end=" ")
            else:
                print(tiles[i][j], end=" ")
        print("\n")


def main():
    tiles:list = [[0 for i in range(7)] for j in range(5)]
    TOTAL_ACTION: int = 0
    TOTAL_collect: int = 0
    
    testTime: int = int(input("Enter the testing time: "))
    
    for test in range(testTime):
        environmenCreate(tiles)
        # print(tiles)
        isReadyTocollect: bool = True
        prev_pos: int = -1
        init_pos: list = randomPosition()
        # print(init_pos)

        action: list = []
        move: list = []
        collect: list = []

        column: int = init_pos[1] #column
        row: int = init_pos[0] #row
        prev_pos: int = -1

        collectObj(tiles, row, column, action, collect)
        showingMovement(row, column, tiles)
        while(isReadyTocollect):
            new_pos: list = randomMove(column, row, action, move, prev_pos)
            column = new_pos[1]
            row = new_pos[0]
            prev_pos = new_pos[2]
            collectObj(tiles, row, column, action, collect)
            showingMovement(row, column, tiles)
            if(column <= 0 or column >= 6 or row <= 0 or row >= 4):
                print("!!!!!!Found Edge! Stopping....!!!!!\n")
                break
        
        totalActionInStep: int = 0
        for a in action:
            totalActionInStep+= a
        
        TOTAL_ACTION += totalActionInStep

        print("\nTotal action =",totalActionInStep)

        totalMoveInStep: int = 0
        for m in move:
            totalMoveInStep += m
        
        print("\nTotal move =", totalMoveInStep)

        totalcollectInStep: int = 0
        for c in collect:
            totalcollectInStep += c

        TOTAL_collect += totalcollectInStep
        
        print("\nTotal collect =", totalcollectInStep)

        if(totalcollectInStep != 0):
            performanceInStep: int = totalActionInStep / totalcollectInStep
        else:
            performanceInStep = 0
        
        print(f"\nPerformance in step {test+1} =", performanceInStep,"\n\n")

    if(TOTAL_collect != 0):
        performanceTotal: int = TOTAL_ACTION / TOTAL_collect
    else:
        performanceTotal = 0

    print(f"\nTotal performance =", performanceTotal,"\n\n")

 
if __name__ == "__main__":
    main()