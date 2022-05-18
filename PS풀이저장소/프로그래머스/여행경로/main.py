is_terminated = False
def backtrack(num, start):
    # print(num, start)
    global is_terminated
    if num == num_tickets:
        is_terminated = True
        return
    if not cities[start][1] or is_terminated:
        return
    for city in routes[cities[start][0]]:
        if not city[1]:
            city[1] = not(city[1])
            next = city[0]
            answer.append(next)
            cities[start][1] -= 1
            backtrack(num+1, next)
            if is_terminated:
                break
            answer.pop()
            city[1] = False
            cities[start][1] += 1
        
def solution(tickets):
    global answer, cities, num_tickets, routes
    answer = []
    cities = {}
    index = 0
    num_tickets = len(tickets)    
    routes = [[] for _ in range(2 * num_tickets)]
    for ticket in tickets:
        a, b = ticket
        if a not in cities:
            cities[a] = [index, 1]
            index += 1
        else:
            cities[a][1] += 1
        if b not in cities:
            cities[b] = [index, 0]
            index += 1
        
        routes[cities[a][0]].append([b, False])
    for i in range(2 * num_tickets):
        routes[i].sort()
    answer.append('ICN')
    backtrack(0, 'ICN')    
    # print(routes)
    # print(cities)
    # print(answer)
    return answer