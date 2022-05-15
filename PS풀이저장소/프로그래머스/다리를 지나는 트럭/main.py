from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = deque([])
    while True:
        # print(truck_weights, on_bridge, answer)
        if on_bridge and on_bridge[0][0] == bridge_length:
            on_bridge.popleft()
            if not truck_weights and not on_bridge:
                answer += 1
                break
        if truck_weights:
            # print('합 : {}, 첫번째 원소 : {}'.format(sum(list(map(lambda x : x[1], on_bridge))), truck_weights[0]))
            if (len(on_bridge) + 1 <= bridge_length) and (sum(list(map(lambda x : x[1], on_bridge))) + truck_weights[0] <= weight):
                on_bridge_truck_weight = truck_weights.pop(0)
                on_bridge.append([0, on_bridge_truck_weight])
        for i in range(len(on_bridge)):
            on_bridge[i][0] += 1
        answer += 1
    return answer