N, M = map(int, input().split())
board = []
result = []
for i in range(N):
    board.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        white = 0
        black = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        white += 1
                    else:
                        black += 1
                else:
                    if board[a][b] != 'W':
                        black += 1
                    else:
                        white += 1

        result.append(white)
        result.append(black)
print(min(result))
                    
