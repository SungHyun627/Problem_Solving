inputs = [["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"], ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]]

def solution(commands):
    # 최대 50×50이므로 ID는 1..50*50 범위 사용 가능
    def to_id(r, c):
        return (r - 1) * 50 + (c - 1)

    # parent & value 초기화
    parent = [i for i in range(50*50)]
    value = ["EMPTY"] * (50*50)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        # 대표를 ra 쪽으로 합친다고 가정
        # 값 처리: 만약 하나에만 값 있다면 그 값을 대표에 남김
        if value[ra] == "EMPTY" and value[rb] != "EMPTY":
            value[ra] = value[rb]
        parent[rb] = ra

    def unmerge(r, c):
        idx = to_id(r, c)
        root = find(idx)
        # 그룹의 기존 값
        grp_value = value[root]
        # 그 그룹에 속한 모든 셀 찾기
        members = [i for i in range(50*50) if find(i) == root]
        for m in members:
            parent[m] = m
            value[m] = "EMPTY"
        # (r, c)는 grp_value 유지
        value[idx] = grp_value

    def update_cell(r, c, val):
        idx = to_id(r, c)
        root = find(idx)
        value[root] = val

    def update_value(v1, v2):
        for i in range(50*50):
            if value[i] == v1:
                value[i] = v2

    answer = []
    for cmd in commands:
        parts = cmd.split()
        op = parts[0]
        if op == "UPDATE":
            if len(parts) == 4:
                r, c, v = int(parts[1]), int(parts[2]), parts[3]
                update_cell(r, c, v)
            else:
                v1, v2 = parts[1], parts[2]
                update_value(v1, v2)
        elif op == "MERGE":
            r1, c1, r2, c2 = map(int, parts[1:5])
            union(to_id(r1, c1), to_id(r2, c2))
        elif op == "UNMERGE":
            r, c = int(parts[1]), int(parts[2])
            unmerge(r, c)
        elif op == "PRINT":
            r, c = int(parts[1]), int(parts[2])
            root = find(to_id(r, c))
            answer.append(value[root])

    return answer


for input in inputs:
  print(solution(input))