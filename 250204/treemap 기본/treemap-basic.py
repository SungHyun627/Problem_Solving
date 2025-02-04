from sortedcontainers import SortedDict

n = int(input())
x = SortedDict()


for _ in range(n):
    commands = input().split()
    op = commands.pop(0)

    if op == 'add':
        key = int(commands[0])
        value = int(commands[1])
        x[key] = value
    elif op == 'remove':
        key = int(commands[0])
        del x[key]
    elif op == 'find':
        key = int(commands[0])
        if key not in x:
            print(None)
        else:
            print(x[key])
    else:
        if len(x) == 0:
            print(None)
        else:
            values = []
            for key, value in x.items():
                values.append(value)
            print(*values)
