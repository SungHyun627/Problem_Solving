def solution(triangle):
    row_num = len(triangle)
    for i in range(1, row_num):
        for j in range(i+1):
            if j == 0:
                triangle[i][0] += triangle[i-1][0]
            elif j == i:
                triangle[i][i] += triangle[i-1][i-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])     
    
    return max(triangle[-1])