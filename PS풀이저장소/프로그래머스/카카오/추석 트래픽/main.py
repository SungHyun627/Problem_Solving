#초당 최대 처리량(1초간 처리하는 요청의 최대 개수)
def convert_to_ms(x):
    a = x.split(':')
    b = a[2].split('.')
    
    return int(a[0]) * 3600 * 1000 + int(a[1])*60*1000 + int(b[0])*1000 + int(b[1])
def solution(lines):
    answer = 0
    lines_len = len(lines)
    regions = []
    for line in lines:
        a = line.split()
        s = convert_to_ms(a[1])
        t = int(float(a[2][:-1]) * 1000)
        regions.append((s-t+1, s))

    for i in range(lines_len):
        count1, count2, count3, count4 = 0, 0, 0, 0
        temp1, temp2 = (regions[i][0]+999), (regions[i][1]+999)
        temp3, temp4 = (regions[i][0]-999), (regions[i][1]-999)
        
        for j in range(lines_len):
            if regions[j][0] > temp1 or regions[j][1] < regions[i][0]:
                continue
            count1 += 1
        for j in range(lines_len):
            if regions[j][0] > temp2 or regions[j][1] < regions[i][1]:
                continue
            count2 += 1
        for j in range(lines_len):
            if regions[j][1] < temp3 or regions[j][0] > regions[i][0]:
                continue
            count3 += 1
        for j in range(lines_len):
            if regions[j][1] < temp4 or regions[j][0] > regions[i][1]:
                continue
            count4 += 1
            

        answer = max(count1, count2, count3, count4, answer)    
    return answer