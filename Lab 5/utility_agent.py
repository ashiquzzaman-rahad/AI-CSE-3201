import random
import math
from collections import deque
import matplotlib.pyplot as plt
import numpy as np


def environmenCreate(world: list) -> None:
    """Creates the world with black space, objects and hurdles"""
    # for i in range(5):
    #     for j in range(7):
    #         world[i][j] = random.choice([0,0,1,9,0,1])

    world = [
        [0,0,0,0,0,0,0],
        [0,0,0,9,0,0,0],
        [0,1,9,9,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]
    
    return world


def detectingObjPos(world: list) -> list:
    """Returns the list of all the objects' rows and columns"""
    objPosRow: list = []
    objPosCol: list = []
    for i in range(5):
        for j in range(7):
            if world[i][j] == 1:
                objPosRow.append(i)
                objPosCol.append(j)
    return objPosRow, objPosCol



def detectingHurdles(world: list) -> list:
    """Returns the list of all the hurdles' rows and columns"""
    hurdlePosRow: list = []
    hurdlePosCol: list = []
    for i in range(5):
        for j in range(7):
            if world[i][j] == 9:
                hurdlePosRow.append(i)
                hurdlePosCol.append(j)
    return hurdlePosRow, hurdlePosCol



def randomInitPosition(world: list) -> list:
    """Returns a random initial position row and column"""
    # a: int = math.floor(random.random() * 3) + 1 #row
    # b: int = math.floor(random.random() * 5) + 1 #column

    # while world[a][b] == 9 or world[a][b] == 1:
    #     a = math.floor(random.random() * 3) + 1
    #     b = math.floor(random.random() * 5) + 1

    a = int(input("a: "))
    b = int(input("b: "))
    return a, b


def closestObjPos(objPosRow: list, objPosCol: list, row: int, column: int) -> int:
    """Returns the closest object's row and column"""
    minDist: int = 99999
    closestObjRow: int = -1
    closestObjCol: int = -1
    for i in range(len(objPosRow)):
        dist: int = abs(row - objPosRow[i]) + abs(column - objPosCol[i])
        # print(dist)
        if minDist >= dist:
            minDist = dist
            closestObjRow = objPosRow[i]
            closestObjCol = objPosCol[i]
    return closestObjRow, closestObjCol


def collectObj(world: list, row: int, column: int, action: list, collect: list, closestObjRow: int, closestObjCol: int) -> None:
    """Collects the objects(replace 1 with 0)"""
    # print(row, column)
    if world[row][column] == 0:
        dist: int = abs(row - closestObjRow) + abs(column - closestObjCol)
        print(f"Distance from closest object is {dist}.")
    else:
        print(f"Object at ({row},{column}) is being collected...")
        action.append(1)
        collect.append(1)
        world[row][column] = 0


def pathSelection(world: list, column: int, row: int, closestObjRow: int, closestObjCol: int) -> list:
    """Returns the shortest path if exists"""
    start = (row, column)
    queue = deque([(start, 0)])
    visited = set([start])
    queue = deque([(start, [])])
    hurdleAvoided: int = 0
    
    while queue:
        (x, y), path = queue.popleft()
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < 5 and 0 <= ny < 7:
                if world[nx][ny] == 9:
                    hurdleAvoided += 1
                if world[nx][ny] == 0 and (nx, ny) not in visited:
                    queue.append(((nx, ny), path + [(x, y)]))
                    visited.add((nx, ny))
                if nx == closestObjRow and ny == closestObjCol:
                    return path + [(x, y), (nx, ny)], hurdleAvoided       
    return [], hurdleAvoided



def plot_world(world, robot_row, robot_col):
    plt.clf()
    fig, ax = plt.subplots()
    
    ax.imshow(world, cmap='gray_r', interpolation='none')
    for r in range(len(world)):
        for c in range(len(world[0])):
            if world[r][c] == 1:
                ax.scatter(c, r, color='blue', s=100, label='Object')

                
    ax.scatter(robot_col, robot_row, color='red', s=400, label='Robot')
    
    ax.imshow(world, cmap='gray_r', interpolation='none')
    ax.set_xticks(np.arange(-0.5, len(world[0]), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(world), 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
    plt.pause(3)
    


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



def main():
    world:list = [[0 for i in range(7)] for j in range(5)]
    objPosRow: list = []
    objPosCol: list = []
    testTime: int = int(input("Enter the testing time: "))

    for test in range(testTime):
        world = environmenCreate(world) 
        closestObjRow: int = -1
        closestObjCol: int = -1
        isCollecting: bool = True
        row, column  = randomInitPosition(world)
        action: list = []
        collect: list = []
        isEdge: bool = False

        while(isCollecting):
            objPosRow, objPosCol = detectingObjPos(world)
            if(len(objPosRow) == 0):
                break
            if isEdge:
                break
            closestObjRow, closestObjCol= closestObjPos(objPosRow, objPosCol, row, column) 
            print(f"Closest Obj Position: {closestObjRow},{closestObjCol}")
            path, hurdleAvoided = pathSelection(world, column, row, closestObjRow, closestObjCol)
            if len(path) == 0:
                print("!!!!Blocked by hurdle...Stopping....!!!")
                break
            
            print(f"This path avoids {hurdleAvoided} hurdles...")
            for i in range(len(path)):
                print(f"{path[i]}",end="")
                if i < len(path) - 1:
                    print(" -> ",end="")
            print()
            ipath = 1
            showingMovement(row, column, world)
            while(ipath < len(path)):
                row, column = path[ipath]
                plot_world(world, row, column)
                collectObj(world, row, column, action, collect, closestObjRow, closestObjCol)
                showingMovement(row, column, world)
                if (column <= 0 or column >= 6 or row <= 0 or row >= 4):
                    print("!!!!!!Found Edge! Stopping....!!!!!\n")
                    isEdge = True
                    break
                ipath += 1

if __name__ == "__main__":
    main()