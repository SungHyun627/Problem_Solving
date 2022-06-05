from collections import Counter
def solution(prices):
    answer = []
    prices_length = len(prices)
    for i in range(prices_length):
        num = 0
        for j in range(i+1, prices_length):
            num += 1
            if prices[j] < prices[i]:
                break
        answer.append(num)
    return answer