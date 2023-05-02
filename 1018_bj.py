N, M = map(int, input().split())

board = []
count = []

for _ in range(N):
    board.append(input())

for x in range(N-7): # 8*8
    for y in range(M-7):
        W_index = 0
        B_index = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j)%2 == 0: # Even
                    if board[i][j] != 'W': # black
                        W_index += 1
                    else: # white
                        B_index += 1
                else: # Odd
                    if board[i][j] != 'W':
                        B_index += 1
                    else:
                        W_index += 1
        
        count.append(W_index)
        count.append(B_index)

print(min(count))
