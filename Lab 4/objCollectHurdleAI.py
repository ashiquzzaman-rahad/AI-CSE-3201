import random
import math
import time


def environmenCreate(world: list) -> None:
    # for i in range(5):
    #     for j in range(7):
            # world[i][j] = random.choice([0,0,1,9,9,1,1])
    world = [
        [0,0,0,0,0,0,0],
        [0,0,0,9,0,0,0],
        [0,1,9,9,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]
    
    return world
    


def detectingObjPos(world: list) -> list|list:
    objPosRow: list = []
    objPosCol: list = []
    for i in range(5):
        for j in range(7):
            if world[i][j] == 1:
                objPosRow.append(i)
                objPosCol.append(j)
    return objPosRow, objPosCol


def randomPosition(world: list) -> list:
    # a: int = math.floor(random.random() * 3) + 1 #row
    # b: int = math.floor(random.random() * 5) + 1 #column

    # while world[a][b] == 9 or world[a][b] == 1:
    #     a = math.floor(random.random() * 3) + 1
    #     b = math.floor(random.random() * 5) + 1
    a = int(input("a: "))
    b = int(input("b: "))

    return [a, b]

                
def closestObjPos(objPosRow: list, objPosCol: list, row: int, column: int) -> int|int:
    minDist: int = 99999
    closestObjRow: int = -1
    closestObjCol: int = -1
    for i in range(len(objPosRow)):
        dist: int = abs(row - objPosRow[i]) + abs(column - objPosCol[i])
        print(dist)
        if minDist > dist:
            minDist = dist
            closestObjRow = objPosRow[i]
            closestObjCol = objPosCol[i]
    return closestObjRow, closestObjCol


def collectObj(world: list, row: int, column: int, action: list, collect: list, closestObjRow: int, closestObjCol: int) -> None:
    # print(row, column)
    if world[row][column] == 0:
        dist: int = abs(row - closestObjRow) + abs(column - closestObjCol)
        print(f"Distance from closest object is {dist}.")
    else:
        print(f"Object at ({row},{column}) is being collected...")
        action.append(1)
        collect.append(1)
        world[row][column] = 0


def checkHurdleLessMove(world: list, column: int, row: int, prev_pos: int, closestObjRow: int, closestObjCol: int) -> list:
    up_col: int = column
    up_row: int = row - 1

    down_col: int = column
    down_row: int = row + 1

    left_col: int = column - 1
    left_row: int = row

    right_col: int = column + 1
    right_row: int = row

    curr_dist: int = abs(row - closestObjRow) + abs(column - closestObjCol)
    left_dist: int = abs(left_row - closestObjRow) + abs(left_col - closestObjCol)
    right_dist: int = abs(right_row - closestObjRow) + abs(right_col - closestObjCol)
    up_dist: int = abs(up_row - closestObjRow) + abs(up_col - closestObjCol)
    down_dist: int = abs(down_row - closestObjRow) + abs(down_col - closestObjCol)

    choicesMove: list = []
    if (world[left_row][left_col] != 9 and prev_pos != 0 and left_dist < curr_dist):
        for i in range(3):
            choicesMove.append(0) 

    if (world[up_row][up_col] != 9 and prev_pos != 1 and up_dist < curr_dist):
        for i in range(3):
            choicesMove.append(1) 

    if (world[right_row][right_col] != 9 and prev_pos != 2 and right_dist < curr_dist):
        for i in range(3):
            choicesMove.append(2) 

    if (world[down_row][down_col] != 9 and prev_pos != 3 and down_dist < curr_dist):
        for i in range(3):
            choicesMove.append(3) 
        
    if len(choicesMove) == 0:
        if (world[left_row][left_col] != 9 and prev_pos != 0):
            for i in range(3):
                choicesMove.append(0) 

        if (world[up_row][up_col] != 9 and prev_pos != 1):
            for i in range(3):
                choicesMove.append(1) 

        if (world[right_row][right_col] != 9 and prev_pos != 2):
            for i in range(3):
                choicesMove.append(2) 

        if (world[down_row][down_col] != 9 and prev_pos != 3):
            for i in range(3):
                choicesMove.append(3)

    return choicesMove


def randomMove(choiceList: list, column: int, row: int, action: list, move: list, prev_pos: int) -> list:
    moveChoice: int = random.choice(choiceList)
    while(prev_pos == moveChoice):
        moveChoice = random.choice(choiceList)

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
        case _: #anything else
            print("invalid!")

    action.append(1)
    move.append(1)
    return [row, column, prev_pos]


def showingMovement(row, column, world):
    for i in range(5):
        for j in range(40):
            print("-", end='')
        print('')
        for j in range(7):
            print('|', end=" ")
            if(i == row and j == column):
                print("#", end=" ")
            else:
                print(world[i][j], end=" ")
            print('|', end=" ")
        print('\n', end="")
    for j in range(40):
        print("-", end='')
    print("\n")

def possibleMoves(choiceList: list) -> None:
    if 0 in choiceList:
        print('left', end=" ")
    if 1 in choiceList:
        print('up', end=" ")
    if 2 in choiceList:
        print('right', end=" ")
    if 3 in choiceList:
        print('down', end=" ")
    print("\n")

    

def main():
    world:list = [[0 for i in range(7)] for j in range(5)]
    objPosRow: list = []
    objPosCol: list = []
    TOTAL_ACTION: int = 0
    TOTAL_COLLECT: int = 0
    
    testTime: int = int(input("Enter the testing time: "))

    for test in range(testTime):
        world = environmenCreate(world) 
        print(world) 
        closestObjRow: int = -1
        closestObjCol: int = -1
        isCollecting: bool = True
        prev_pos: int = -1
        init_pos: list = randomPosition(world)
        action: list = []
        move: list = []
        collect: list = []
        column: int = init_pos[1] #column
        row: int = init_pos[0] #row
        edgeFlag: bool = False
        hurdleFlag: bool = False

        print(f"Initial Position: {row},{column}")
        showingMovement(row,column,world)
        step = 0
        while(isCollecting):
            if step != 0:
                print(f"Extra moves: {step - init_dist}")
            objPosRow, objPosCol = detectingObjPos(world)
            if(len(objPosRow) == 0):
                break
            # print(objPosRow)
            # print(objPosCol)
            closestObjRow, closestObjCol= closestObjPos(objPosRow, objPosCol, row, column) 
            print(f"Closest Obj Position: {closestObjRow},{closestObjCol}")
            init_dist = abs(row - closestObjRow) + abs(column - closestObjCol)
            if (edgeFlag or hurdleFlag):
                break
            step = 0
            while(world[closestObjRow][closestObjCol] != 0):
                choiceList: list = checkHurdleLessMove(world, column, row, prev_pos,closestObjRow, closestObjCol)
                possibleMoves(choiceList)
                if len(choiceList) == 0:
                    print("!!!!!!Blocked By Hurdle! Stopping....!!!!!\n")
                    hurdleFlag = True
                    break
                new_pos: list = randomMove(choiceList, column, row, action, move, prev_pos)
                column = new_pos[1]
                row = new_pos[0]
                prev_pos = new_pos[2]
                print(f"Current Position: {row},{column}")
                collectObj(world, row, column, action, collect, closestObjRow, closestObjCol)
                showingMovement(row, column, world)
                step += 1
                time.sleep(2)

                if (column <= 0 or column >= 6 or row <= 0 or row >= 4):
                    print("!!!!!!Found Edge! Stopping....!!!!!\n")
                    edgeFlag = True
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

        totalCollectInStep: int = 0
        for c in collect:
            totalCollectInStep += c

        TOTAL_COLLECT += totalCollectInStep
        
        print("\nTotal collect =", totalCollectInStep)

        if(totalCollectInStep != 0):
            performanceInStep: int = totalActionInStep / totalCollectInStep
        else:
            performanceInStep = 0
        
        print(f"\nPerformance in step {test+1} =", performanceInStep,"\n\n")

    if(TOTAL_COLLECT != 0):
        performanceTotal: int = TOTAL_ACTION / TOTAL_COLLECT
    else:
        performanceTotal = 0

    print(f"\nTotal performance =", performanceTotal,"\n\n")
        

if __name__ == "__main__":
    main()