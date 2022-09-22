def solution(n, k, cmd):
    global arr
    answer = ['O'] * n
    cur = k
    arr = [[i-1, i+1] for i in range(n)]
    arr[n-1][1] = 0
    erases = []
    for c in cmd:
        command = ''
        num = 0
        a = c.split()
        if len(a) == 1:
            command = a[0]
        else:
            command, num = a[0], int(a[1])
        #print(command, num)
        if num:
            if command == "U":
                for _ in range(num):
                    cur = arr[cur][0]
            else:
                for _ in range(num):
                    cur = arr[cur][1]
        else:
            if command == 'C':
                front, back = arr[cur][0], arr[cur][1]
                arr[front][1] = back
                arr[back][0] = front
                erases.append(cur)
                answer[cur] = 'X'
                if back:
                    cur = back
                else:
                    cur = front
            else:
                idx = erases.pop()
                arr[arr[idx][0]][1] = idx
                arr[arr[idx][1]][0] = idx
                answer[idx] = 'O'
        #print(cur, answer)
    return ''.join(answer)