def convert_str_to_time(x):
    a, b = map(int, x.split(':'))
    return a * 60 + b

def solution(fees, records):
    temp = []
    cars_history = {}
    std_time, std_fee, unit_time, unit_fee = fees
    
    for record in records:
        time, car_num, in_out = record.split()
        #누적, 시간, 인/아웃
        time = convert_str_to_time(time)
        car_num = int(car_num)
        
        if car_num in cars_history:
            #기록이 있는데 입차인 경우
            if cars_history[car_num][2] == "IN":
                #시간 계산 후, 누적 후, OUT으로 변경
                cars_history[car_num][0] += (time - cars_history[car_num][1])
                cars_history[car_num][1] = 0
                cars_history[car_num][2] = "OUT"
            #기록이 있는데 출차인 경우
            else:
                #시간 계산 후, IN으로 변경
                cars_history[car_num][1] = time
                cars_history[car_num][2] = "IN"
        else:
            #기록이 없는 경우
            cars_history[car_num] = [0, time, 'IN']
	
    #계산
    for num in cars_history.keys():
        total_fee = 0
        if cars_history[num][2] == "IN":
            cars_history[num][0] += (23 * 60 + 59 - cars_history[num][1])
        a = cars_history[num][0]
        
        if a <= std_time:
            total_fee = std_fee
        else:
            if (a - std_time) % unit_time:
                additional_fee  = (int((a-std_time) // unit_time) + 1) * unit_fee
            else:
                additional_fee  = int((a-std_time) // unit_time) * unit_fee
            total_fee = std_fee + additional_fee
        temp.append((num, total_fee))
        temp.sort(key = lambda x: x[0])
    return [i[1] for i in temp]