def solution(operations):
    a = []
    for operation in operations:
        command, number = operation.split()
        if command == 'I':
            a.append(int(number))
        else:
            if not a:
                continue
            a.sort()
            if number == '-1':
                a = a[1:]
            else:
                a = a[:-1]
    a.sort()
    if not a:
        return [0, 0]
    else:
        return [a[-1], a[0]]