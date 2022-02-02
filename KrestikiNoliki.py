board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
win_combinations = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],[(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
combo_1 = [(0,0),(0,1),(0,2)]
def print_board():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j] + " ", end="")
        print("\n")

def make_step(sign):
    print('Пользователь, который играет '+ sign)
    print('Введите номер строки:')
    i = int(input())
    if i < 0 or i >= 3:
        print('Числа не входят в заданный диапазон')
        make_step(sign)
    print('Введите номер столбца:')
    j = int(input())
    if j < 0 or j >= 3:
        print('Числа не входят в заданный диапазон')
        make_step(sign)
    if board[i][j] != '-':
        print('Данная ячейка уже занята, введите другие координаты')
        make_step(sign)
    board[i][j] = sign
    print_board()

def check_winner():
    for i in range(len(win_combinations)):
        combo = win_combinations[i]
        a0 = combo[0]
        value0 = board[a0[0]][a0[1]]
        a1 = combo[1]
        value1 = board[a1[0]][a1[1]]
        a2 = combo[2]
        value2 = board[a2[0]][a2[1]]
        if value0 == value1 == value2 and value0 != '-':
            print('Победил игрок ' + value0)
            return True
        else:
            return False

while True:
    make_step('X')
    if check_winner():
        break
    make_step('0')
    if check_winner():
        break



