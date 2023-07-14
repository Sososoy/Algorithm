cnt = [0] * (41)
cnt [0] = 0
cnt[1] = 1

for i in range(2, 41):
    cnt[i] = cnt[i - 1] + cnt[i - 2]

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 0:
        print("1 0")
    else:
        print(cnt[n-1], cnt[n])