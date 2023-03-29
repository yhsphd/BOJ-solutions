# WIP
row = ["WB" * 4, "BW" * 4]
chess = [[row[0], row[1]] * 4, [row[1], row[0]] * 4]

size = int(input().split()[0])
board = []

for i in range(size):
    board.append(input())

# for i in range(len(board[0])-len(chess[0])):
