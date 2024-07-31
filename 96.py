def read_sudoku_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    puzzles = []
    current_puzzle = []

    for line in lines:
        line = line.strip()
        if line.startswith("Grid"):
            if current_puzzle:
                puzzles.append(current_puzzle)
                current_puzzle = []
        else:
            current_puzzle.append([int(char) for char in line])

    if current_puzzle:
        puzzles.append(current_puzzle)

    return puzzles

# Example usage
file_path = 'tempsudoku.txt'  # Replace with your file path
puzzles = read_sudoku_file(file_path)

def get_block(row, col):
    if row < 3:
        if col < 3:
            return 1
        elif col > 5:
            return 3
        else: 
            return 2 
    elif row > 5:
        if col < 3:
            return 7
        elif col > 5:
            return 9
        else: 
            return 8
    else:
        if col < 3:
            return 4
        elif col > 5:
            return 6
        else: 
            return 5

def get_block_cells(block_id):
    if block_id == 1:
        return [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    elif block_id == 2:
        return [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]
    elif block_id == 3:
        return [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)]
    elif block_id == 4:
        return [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
    elif block_id == 5:
        return [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
    elif block_id == 6:
        return [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)]
    elif block_id == 7:
        return [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)]
    elif block_id == 8:
        return [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)]
    elif block_id == 9:
        return [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]

def mark_filled(aux, row, col, digit):
    for cell in get_block_cells(get_block(row, col)):
        aux[cell[0]][cell[1]][digit] = -1
    for k in range(0, 9):
        aux[row][k][digit] = -1
    for k in range(0, 9):
        aux[k][col][digit] = -1
    for dig in range(1, 10):
        aux[row][col][dig] = -1
    # if aux[6][1][4] == -1:
    #     print("yaha seeee: ", row, col, digit, get_block_cells(get_block(row, col)))

def print_aux(aux):
    # Check aux situation
    for i in range(1, 10):
        if i != 4:
            continue
        print(f"for digit {i}")
        for j in range(0, 9):
            for k in range(0, 9):
                print(aux[j][k][i], end=' ')
            print()
        print("")

def check_naked_singles(aux, puzzle):
    found = 0
    print("here")
    print_aux(aux)
    for row in range(0, 9):
        for col in range(0, 9):
            if puzzle[row][col] == 0:
                possible = set()
                for dig in range(1, 10):
                    if aux[row][col][dig] != -1:
                        possible.add(dig)
                    for i in range(0, 9):
                        if puzzle[row][i] != 0 and puzzle[row][i] in possible:
                            possible.remove(puzzle[row][i])
                        if puzzle[i][col] != 0 and puzzle[i][col] in possible:
                            possible.remove(puzzle[i][col])
                    for cell in get_block_cells(get_block(row, col)):
                        if puzzle[cell[0]][cell[1]] != 0 and puzzle[cell[0]][cell[1]] in possible:
                            possible.remove(puzzle[cell[0]][cell[1]])
                if len(possible) == 1:
                    puzzle[row][col] = list(possible)[0]
                    mark_filled(aux, row, col, puzzle[row][col])
                    print(f"Filleddddddddddddddddddddddddddddddd 4: {puzzle[row][col]} in {(row, col)}")
                    found += 1
    return found

def generate_possibilities(aux, puzzle):
    for row in range(0, 9):
        for col in range(0, 9):
            if puzzle[row][col] == 0:
                possible = set()
                for dig in range(1, 10):
                    if aux[row][col][dig] != -1:
                        possible.add(dig)
                    for i in range(0, 9):
                        if puzzle[row][i] != 0 and puzzle[row][i] in possible:
                            possible.remove(puzzle[row][i])
                        if puzzle[i][col] != 0 and puzzle[i][col] in possible:
                            possible.remove(puzzle[i][col])
                    for cell in get_block_cells(get_block(row, col)):
                        if puzzle[cell[0]][cell[1]] != 0 and puzzle[cell[0]][cell[1]] in possible:
                            possible.remove(puzzle[cell[0]][cell[1]])                
                print(row, col, possible)


puzzle_count = 1
for puzzle in puzzles:
    aux = [[[0 for i in range(10)] for j in range(10)] for k in range(10)]
    print_aux(aux)
    empty_cells_count = 0
    for row in range(0, 9):
        for col in range(0, 9):
            digit = puzzle[row][col]
            if digit != 0:
                mark_filled(aux, row, col, digit)
            else:
                empty_cells_count += 1

    print(f"Gridddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd {puzzle_count}")
    print_aux(aux)

    while empty_cells_count > 0:
        found_any = False
        # print(empty_cells_count)
        for digit in range(1, 10):
            # check if any row has empty cell
            # num = random.random()
            # print(digit, num)
            for row in range(0, 9):
                possible = 0
                empty_cell = ()
                for col in range(0, 9):
                    if aux[row][col][digit] == 0:
                        possible += 1
                        empty_cell = (row, col)
                if possible == 1:
                    empty_cells_count -= 1
                    puzzle[empty_cell[0]][empty_cell[1]] = digit
                    mark_filled(aux, empty_cell[0], empty_cell[1], digit)
                    print(f"Filleddddddddddddddddddddddddddddddd 1: {digit} in {empty_cell}")
                    print_aux(aux)
                    found_any = True
            # print("r")
            for col in range(0, 9):
                possible = 0
                empty_cell = ()
                for row in range(0, 9):
                    if aux[row][col][digit] == 0:
                        possible += 1
                        empty_cell = (row, col)
                if possible == 1:
                    empty_cells_count -=1
                    puzzle[empty_cell[0]][empty_cell[1]] = digit
                    mark_filled(aux, empty_cell[0], empty_cell[1], digit)
                    print(f"Filleddddddddddddddddddddddddddddd 2: {digit} in {empty_cell}")
                    print_aux(aux)
                    found_any = True
            # print("c")
            for block in range(1, 10):
                possible = 0
                empty_cell = ()
                for cell in get_block_cells(block):
                    if aux[cell[0]][cell[1]][digit] == 0:
                        possible += 1
                        empty_cell = (cell[0], cell[1])
                # if digit == 6 and block == 7:
                #     print(possible)
                if possible == 1:
                    empty_cells_count -=1
                    puzzle[empty_cell[0]][empty_cell[1]] = digit
                    mark_filled(aux, empty_cell[0], empty_cell[1], digit)
                    print(f"Filledddddddddddddddddddddddddddd 3: {digit} in {empty_cell}")
                    print_aux(aux)
                    found_any = True
        
        if found_any == False and empty_cells_count > 0:
            result = check_naked_singles(aux, puzzle)
            empty_cells_count -= result
            if result == 0:
                generate_possibilities(aux, puzzle)
                exit(0)
                # try something else
                pass
                

    print(f"Solved matrix: {puzzle_count}")
    for i in range(0, 9):
        for j in range(0, 9):
            print(puzzle[i][j], end='')
        print()
    puzzle_count +=1



# check for naked singles, naked paur, naked triple etc

