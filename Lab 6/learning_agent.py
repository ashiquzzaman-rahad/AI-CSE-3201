import random
import copy
import matplotlib.pyplot as plt
import numpy as np

def create_environment() -> list:
    """Creates a random 5X5 world(list) which has 1 for object and 0 for free space"""
    world: list = [[0 for i in range(5)] for j in range(5)]
    for i in range(5):
        for j in range(5):
            world[i][j] = random.choice([0,1,0])
    return world


def find_object_positions(world: list) -> list:
    """Returns the list of objects postions as (row, column)"""
    object_pos: list = []
    for i in range(5):
        for j in range(5):
            if world[i][j] == 1:
                object_pos.append((i, j))
    return object_pos


def train_agent() -> list:
    """Trains the agent with some random world environment. Returns the probabilities list of each index's having the object"""
    train_session: int = 1000
    probability: list = [[0 for i in range(5)] for j in range(5)]
    for i in range(train_session):
        world: list = create_environment()
        object_pos: list = find_object_positions(world)
        for pos in object_pos:
            probability[pos[0]][pos[1]] += 1
        print(probability)
    return probability


def sort_index_probability(probability_learned: list):
    """Sorts the indices in accending order according to their probabilities. Returns the sorted indices' list"""
    values_with_indices = []
    for i in range(5):
        for j in range(5):
            values_with_indices.append((probability_learned[i][j], (i, j)))
    sorted_values_with_indices = sorted(values_with_indices)
    # print(sorted_values_with_indices)
    sorted_indices = []
    for element in sorted_values_with_indices:
        sorted_indices.append(element[1])
    return sorted_indices



def check_performance(world: list, probable_index_sorted: list) -> int:
    """Checks each index of the world according to the sorted index. Returns the number of getting objects(success) and not getting objects(failure)"""
    success: int = 0
    failure: int = 0
    for index in probable_index_sorted:
        row: int = index[0]
        col: int = index[1]
        if world[row][col] == 1:
            success += 1
        else:
            failure += 1
    return (success/25)*100, (failure/25)*100



def show_performance(world: list, probability: list, probable_index: tuple, visited_indices: list) -> None:
    """Shows the steps of checking in a UI"""
    cmap = plt.cm.colors.ListedColormap(['yellow', 'grey']) 
    bounds = [0, 0.5, 1.5] 
    norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

    # plt.clf()
    fig, ax = plt.subplots()
    ax.imshow(world, cmap=cmap, norm=norm, interpolation='none')
    # ax.imshow(world, cmap='gray_r', interpolation='none')
    for r in range(5):
        for c in range(5):
            ax.text(c, r, f'{probability[r][c]}', ha='center', va='center', color='black')
            if (r, c) == probable_index:
                ax.scatter(c, r, color='blue', s=400)
            if (r, c) in visited_indices:
                if world[r][c] == 1: 
                    ax.scatter(c, r, color='green', s=250) 
                elif world[r][c] == 0: 
                    ax.scatter(c, r, color='red', s=250)

    # ax.imshow(world, cmap='gray_r', interpolation='none')
    ax.set_xticks(np.arange(-0.5, len(world[0]), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(world), 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
    plt.show(block=False) 
    plt.pause(1) 
    plt.close(fig)



def main():
    """This is the main functiong"""
    performance_session: int = 2
    probability_learned: list = train_agent()
    probability: list = copy.deepcopy(probability_learned)
    probable_index_sorted = sort_index_probability(probability_learned)
    print(probable_index_sorted)
    # print(probability_learned)

    for i in range(performance_session):
        visited_indices: list = []
        print(f"Performance session: {i+1}")
        world: list = create_environment()

        for j in range(len(probable_index_sorted)-1, -1, -1):
            show_performance(world, probability_learned, probable_index_sorted[j], visited_indices)
            visited_indices.append(probable_index_sorted[j])

        success, failure = check_performance(world, probable_index_sorted)
        print("Success = %.2f%% & failure = %.2f%%" %(success, failure))
        print("\n")
    


if __name__ == "__main__":
    main()