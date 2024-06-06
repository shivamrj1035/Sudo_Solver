import pyautogui as pg
import time

grid = []

# Taking input for the Sudoku grid
while True:
    try:
        row = list(input('Row: '))
        if len(row) != 9:
            raise ValueError("Input must contain exactly 9 digits.")
        ints = [int(n) for n in row]
        grid.append(ints)

        if len(grid) == 9:
            break
        print('Row ' + str(len(grid)) + ' Complete')
    except ValueError as e:
        print(f"Error: {e}")

# Function to check if a number (n) is valid to place at position (x, y) on the grid
def possible(x, y, n):
    for i in range(0, 9):
        if grid[i][x] == n and i != y: # Checks for number (n) in the same column
            return False

    for i in range(0, 9):
        if grid[y][i] == n and i != x: # Checks for number (n) in the same row
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3):  # Checks for numbers in the same 3x3 box
            if grid[Y][X] == n:
                return False
    return True

# Function to type the solution into the active window using PyAutoGUI
def type_soln(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')

# Function to print the Sudoku grid in the console
def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - - -")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end=" ")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j])+" ", end=" ")

# Recursive function to solve the Sudoku grid
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0 # Backtrack if the current choice leads to a dead end
                return
    # Offer options after solving
    while True:
        print('1) Want to print solution in cmd?')
        flag = False
        if flag:
            print('2) Want to solve in sudoku.com ?')
        print('3) Exit')
        choice = input('Enter choice: ')
        if choice == str(1):
            print_board(grid)
            print("Solved successfully..!")
        elif choice == str(2):
            time.sleep(4)
            type_soln(grid)
            flag= True
            print("Solved successfully..!")
        elif choice == '3':
            exit()
        else:
            print('Choose correct option either 1 or 2')

try:
    solve()
except Exception as e:
    print(f"An error occurred: {e}")
