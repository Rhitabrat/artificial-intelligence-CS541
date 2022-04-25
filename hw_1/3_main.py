import random
import pandas as pd

grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]


def display(arr):
    for i in range(3):
        for j in range(3):
            print(arr[i][j], end="  ")
        print()


def get_position(arr):
    for i in range(3):
        for j in range(3):
            if "A" in str(arr[i][j]):
                return arr[i][j][0]


def clean(arr, row, col):
    arr[row][col] = arr[row][col].replace('D','')
    return arr


dirt_pile_count = [1, 3, 5]
performance_count_100 = []

for j in range(100):
    performance_count = []
    for each_pile_count in dirt_pile_count:
        # grid_new = grid.copy()
        grid_new = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

        ######################################################

        # select random dirt positions
        row_indices = [0, 1, 2]
        col_indices = [0, 1, 2]

        for each_pile_position in range(each_pile_count):

            # select random dirt positions
            random_position_row = random.choice(row_indices)
            random_position_col = random.choice(col_indices)

            grid_new[random_position_row][random_position_col] = grid_new[random_position_row][random_position_col] + "D"

            if len(row_indices)-1:
                row_indices.remove(random_position_row)
            else:
                col_indices.remove(random_position_col)

        ######################################################

        # select random agent positions
        random_position_row_agent = random.choice([0, 1, 2])
        random_position_col_agent = random.choice([0, 1, 2])
        grid_new[random_position_row_agent][random_position_col_agent] = grid_new[random_position_row_agent][random_position_col_agent] + "A"

        # print("......Initial Grid......")
        # display(grid_new)
        # print("................")
        ######################################################

        count = 1

        for i in range(100):
            
            # if agent is at 1
            if '1' in grid_new[0][0] and 'A' in grid_new[0][0]:
                prob = random.randint(1, 4)
                if  prob == 1 or prob == 2 or prob == 3:
                    # if it is clean, move the agent
                    if 'D' not in grid_new[0][0]:
                        # go Right
                        grid_new[0][0] = "1"
                        grid_new[0][1] = grid_new[0][1] + "A"

                    # if it is dirty, clean the box
                    elif 'D' in grid_new[0][0] and random.randint(1, 10) != 1:
                        # clean
                        cleaned = str(grid_new[0][0]).replace('D', '')
                        grid_new[0][0] = cleaned

                        # if any('D' in str(x) for x in grid_new):
                    
                # count += 1

            # if agent is at 2
            elif '2' in grid_new[0][1] and 'A' in grid_new[0][1]:
                prob = random.randint(1, 4)
                if  prob == 1 or prob == 2 or prob == 3:
                    # if it is clean, move the agent
                    if 'D' not in grid_new[0][1]:
                        # go Right
                        grid_new[0][1] = "2"
                        grid_new[0][2] = grid_new[0][2] + "A"

                    # if it is dirty, clean the box
                    elif 'D' in grid_new[0][1] and random.randint(1, 10) != 1:
                        # clean
                        cleaned = str(grid_new[0][1]).replace('D', '')
                        grid_new[0][1] = cleaned
                    # count += 1

            # if agent is at 3
            elif '3' in grid_new[0][2] and 'A' in grid_new[0][2]:
                prob = random.randint(1, 4)
                if  prob == 1 or prob == 2 or prob == 3:
                        # if it is clean, move the agent
                        if 'D' not in grid_new[0][2]:
                            # go Down
                            grid_new[0][2] = "3"
                            grid_new[1][2] = grid_new[1][2] + "A"

                        # if it is dirty, clean the box
                        elif 'D' in grid_new[0][2] and random.randint(1, 10) != 1:
                            # clean
                            cleaned = str(grid_new[0][2]).replace('D', '')
                            grid_new[0][2] = cleaned
                        # count += 1

            # if agent is at 4
            elif '4' in grid_new[1][0] and 'A' in grid_new[1][0]:
                prob = random.randint(1, 4)
                if  prob == 1 or prob == 2 or prob == 3:
                    # if it is clean, move the agent
                    if 'D' not in grid_new[1][0]:
                        # go Up or Down

                        if random.randint(1, 2) == 1:
                            # print("Up")
                            # Up
                            grid_new[1][0] = "4"
                            grid_new[0][0] = grid_new[0][0] + "A"
                        else:
                            # print("Down")
                            # Down
                            grid_new[1][0] = "4"
                            grid_new[2][0] = grid_new[2][0] + "A"

                    # if it is dirty, clean the box
                    elif 'D' in grid_new[1][0] and random.randint(1, 10) != 1:
                        # clean
                        cleaned = str(grid_new[1][0]).replace('D', '')
                        grid_new[1][0] = cleaned
                    # count += 1

            # if agent is at 5
            elif '5' in grid_new[1][1] and 'A' in grid_new[1][1]:
                prob = random.randint(1, 4)
                if  prob == 1 or prob == 2 or prob == 3:
                    # if it is clean, move the agent
                    if 'D' not in grid_new[1][1]:
                        # go Left
                        grid_new[1][1] = "5"
                        grid_new[1][0] = grid_new[1][0] + "A"

                    # if it is dirty, clean the box
                    elif 'D' in grid_new[1][1] and random.randint(1, 10) != 1:
                        # clean
                        cleaned = str(grid_new[1][1]).replace('D', '')
                        grid_new[1][1] = cleaned
                    # count += 1

            # if agent is at 6
            elif '6' in grid_new[1][2] and 'A' in grid_new[1][2]:
                prob = random.randint(1, 4)
                if  prob == 1 or prob == 2 or prob == 3:
                    # if it is clean, move the agent
                    if 'D' not in grid_new[1][2]:
                        # go Left
                        grid_new[1][2] = "6"
                        grid_new[1][1] = grid_new[1][1] + "A"

                    # if it is dirty, clean the box
                    elif 'D' in grid_new[1][2] and random.randint(1, 10) != 1:
                        # clean
                        cleaned = str(grid_new[1][2]).replace('D', '')
                        grid_new[1][2] = cleaned
                    # count += 1

            # if agent is at 7
            elif '7' in grid_new[2][0] and 'A' in grid_new[2][0]:
                prob = random.randint(1, 4)
                if  prob == 1 or prob == 2 or prob == 3:
                    # if it is clean, move the agent
                    if 'D' not in grid_new[2][0]:
                        # go Right
                        grid_new[2][0] = "7"
                        grid_new[2][1] = grid_new[2][1] + "A"

                    # if it is dirty, clean the box
                    elif 'D' in grid_new[2][0] and random.randint(1, 10) != 1:
                        # clean
                        cleaned = str(grid_new[2][0]).replace('D', '')
                        grid_new[2][0] = cleaned
                    # count += 1

            # if agent is at 8
            elif '8' in grid_new[2][1] and 'A' in grid_new[2][1]:
                prob = random.randint(1, 4)
                if  prob == 1 or prob == 2 or prob == 3:
                    # if it is clean, move the agent
                    if 'D' not in grid_new[2][1]:
                        # go Right
                        grid_new[2][1] = "8"
                        grid_new[2][2] = grid_new[2][2] + "A"

                    # if it is dirty, clean the box
                    elif 'D' in grid_new[2][1] and random.randint(1, 10) != 1:
                        # clean
                        cleaned = str(grid_new[2][1]).replace('D', '')
                        grid_new[2][1] = cleaned
                    # count += 1

            # if agent is at 9
            elif '9' in grid_new[2][2] and 'A' in grid_new[2][2]:
                prob = random.randint(1, 4)
                if  prob == 1 or prob == 2 or prob == 3:
                    # if it is clean, move the agent
                    if 'D' not in grid_new[2][2]:
                        # go Up
                        grid_new[2][2] = "9"
                        grid_new[1][2] = grid_new[1][2] + "A"

                    # if it is dirty, clean the box
                    elif 'D' in grid_new[2][2] and random.randint(1, 10) != 1:
                        # clean
                        cleaned = str(grid_new[2][2]).replace('D', '')
                        grid_new[2][2] = cleaned     
                    # count += 1   

            # print("................")
            # display(grid_new)
            # print("................")

            if any('D' in str(x) for x in grid_new):
                count += 1


        performance_count.append(count)

    performance_count_100.append(performance_count)


df = pd.DataFrame(performance_count_100, columns=['1','3','5'])

print(df['1'].mean())
print(df['3'].mean())
print(df['5'].mean())