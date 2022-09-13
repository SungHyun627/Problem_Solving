def solution(k, dungeons):
    global answer, dungeon_num, visited, n_dungeons
    n_dungeons = dungeons[:]
    answer, dungeon_num = -1, len(n_dungeons)
    visited = [False] * dungeon_num
    explore_dungeon(k, 0)
    return answer

def explore_dungeon(remain, cnt):
    global answer, dungeon_num, n_dungeons
    answer = max(answer, cnt)
    for i in range(dungeon_num):
        if visited[i]:
            continue
        if n_dungeons[i][0] > remain:
            continue
        visited[i] = True
        explore_dungeon(remain-n_dungeons[i][1], cnt+1)
        visited[i] = False
    