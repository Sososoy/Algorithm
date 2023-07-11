n = int(input())
ball = list(input())

red = ball.count('R')
blue = n - red
answer = min(red, blue)
cnt = 0

for i in range(n):
    if ball[i] != ball[0]:
        break
    cnt += 1

if ball[0] == 'R':
    answer = min(answer, red - cnt)
else: 
    answer = min(answer, blue - cnt)

cnt = 0
for i in range(n-1, -1, -1):
    if ball[i] != ball[n - 1]:
        break
    cnt += 1

if ball[n - 1] == 'R':
    answer = min(answer, red - cnt)
else:
    answer = min(answer, blue - cnt)

print(answer)