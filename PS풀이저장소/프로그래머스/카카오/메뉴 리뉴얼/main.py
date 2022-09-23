from itertools import combinations

def solution(orders, course):
    answer = []
    for i in range(len(orders)):
        orders[i] = list(orders[i])

    for i in course:
        string_count = {}
        for j in range(len(orders)):
            combs = [''.join(k) for k in list(combinations(orders[j], i))]
            # print(combs)
            for k in range(len(combs)):
                combs[k] = ''.join(sorted(list(combs[k])))
                if combs[k] in string_count:
                    string_count[combs[k]] += 1
                else:
                    string_count[combs[k]] = 1
        # print(string_count)
        if not string_count:
            break
        max_count = max(string_count.values())
        # print(max_count)
        for key in string_count.keys():
            if max_count < 2:
                break
            if string_count[key] == max_count:
                answer.append(key)
    answer.sort()
    return answer