class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

tree = {}

# 전위 순회(Preorder Traversal)
def pre_order(node):
    print(node.data, end = ' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

#중위 순회(Inorder Traversal)
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end = ' ')
    if node.left_node != None:
        in_order(tree[node.right_node])

#후위 순회(Postorder Traversal)
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end = ' ')


def find_min_sum(number_str, k):
    n = len(number_str)
    
    # dp[i][j]: 첫 i자리까지 숫자를 j개의 부분으로 나누었을 때 최소 합
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    
    # 숫자 한 자리를 하나로 간주했을 때, 초기값 설정
    for i in range(1, n + 1):
        dp[i][1] = int(number_str[:i])  # 처음부터 i까지의 부분을 한 개로 나눈 값
    
    # 동적 계획법으로 dp 계산
    for j in range(2, k + 1):  # j개의 부분으로 나누기 (2부터 k까지)
        for i in range(j, n + 1):  # i번째 자리까지 계산 (최소 j자리 이상이어야 함)
            # 이전 부분에서 하나를 선택하여 dp값을 갱신
            for l in range(j - 1, i):  # l은 앞부분 끝 위치
                dp[i][j] = min(dp[i][j], dp[l][j - 1] + int(number_str[l:i]))
    
    # 마지막 값이 답 (전체 숫자 문자열을 k개의 부분으로 나눈 최소 합)
    return dp[n][k]

# 예시: 숫자 문자열 "123452"에서 + 기호를 2개 삽입하여 최소 합 구하기
number_str = "123452"
k = 2
result = find_min_sum(number_str, k)
print("최소값:", result)

### 123452 숫자 사이에 +기호 2개를 삽입해서 계산한 값이 최소가 되도록 하는 경우 알려줘
### 주어진 숫자가 n, +의 개수가 k일 때 알려줘