def solution(routes):
    answer = 0
    #카메라 위치
    camera_pos = -30001
    #진출 시점을 기준으로 오름차순 정렬
    routes.sort(key = lambda x: x[1])
    
    for route in routes:
        if route[0] > camera_pos:
            camera_pos = route[1]
            answer += 1
            
    return answer