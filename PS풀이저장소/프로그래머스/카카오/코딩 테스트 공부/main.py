def solution(alp, cop, problems):
    answer = 0
    alp_max = max([i[0] for i in problems])
    cop_max = max([i[1] for i in problems])
    dp = [[301] * (cop_max +1) for _ in range(alp_max + 1)]
    
    alp = min(alp, alp_max)
    cop = min(cop, cop_max)
    dp[alp][cop] = 0
    for i in range(alp, alp_max+1):
        for j in range(cop, cop_max+1):
            if i != alp_max:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j != cop_max:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if i >= alp_req and j >= cop_req:
                    x = min(alp_max, i+alp_rwd)
                    y = min(cop_max, j+cop_rwd)
                    dp[x][y] = min(dp[x][y], dp[i][j] + cost)
    return dp[alp_max][cop_max]