from sys import stdin

N = int(stdin.readline())
queue = []

for i in range(N):
    n = stdin.readline().split()

    if n[0] == 'push':
        queue.append(n[1])
    elif n[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
    elif n[0] == 'size':
        print(len(queue))
    elif n[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif n[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif n[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])