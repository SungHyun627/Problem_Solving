from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

stdin = open('./input.txt', 'r')

#노드의 개수
n = int(stdin.readline())

nodes_inorder = list(map(int, stdin.readline().rstrip().split()))
nodes_postorder = list(map(int, stdin.readline().rstrip().split()))


order_inorder = [0] * (n+1)

#특정 번호의 노드가 inorder로 몇번째 순서로 방문되는 지를 저장하는 리스트
for i in range(n):
    order_inorder[nodes_inorder[i]] = i

pre_order = []

def find_each_tree_parent(inorder_start, inorder_end, postorder_start, postorder_end):

    #재귀 종료 조건
    if (inorder_start > inorder_end) or (postorder_start > postorder_end):
        return
    
    #부모 노드
    parentnode = nodes_postorder[postorder_end]
    pre_order.append(parentnode)

    #부모 노드를 기준으로 왼쪽에 있는 노드 수
    left_nodes_number = order_inorder[parentnode] - inorder_start
    right_nodes_number = inorder_end - order_inorder[parentnode]

    #루트노드를 기준으로 왼쪽 트리에서 동일한 작업 수행
    find_each_tree_parent(inorder_start, inorder_start+left_nodes_number - 1, postorder_start, postorder_start + left_nodes_number - 1)
    #루트노드를 기준으로 오른쪽 트리에서 동일한 작업 수행
    find_each_tree_parent(inorder_end-right_nodes_number+1, inorder_end, postorder_end-right_nodes_number, postorder_end-1)

find_each_tree_parent(0, n-1, 0, n-1)
print(*pre_order)