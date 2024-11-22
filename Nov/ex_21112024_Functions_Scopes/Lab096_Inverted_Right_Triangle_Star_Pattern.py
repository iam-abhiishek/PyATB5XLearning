
num = int(input('enter ur number\n'))
for i in range(0, num):
    for j in range(0, num-i):
        print('*', end='')
    print()