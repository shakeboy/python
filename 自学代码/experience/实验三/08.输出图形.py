for i in range(1, 4):
    for j in range(0, 4 - i):
        print(' ', end='')
    for j in range(0, 2 * i - 1):
        print('*', end='')
    print()
for i in range(0, 7):
    for j in range(0, i):
        print(' ', end='')
    for j in range(0, 7 - 2 * i):
        print('*', end='')
    print()
