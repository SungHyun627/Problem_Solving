n = int(input())
x = dict()
ans = []

for _ in range(n):
    commands = input().split()
    op = commands.pop(0)
    key = int(commands[0])
    if op == 'add':
        value = int(commands[1])
        x[key] = value
    elif op == 'remove':
        del x[key]
    else:
        if key in x:
            print(x[key])
        else:
            print(None)
