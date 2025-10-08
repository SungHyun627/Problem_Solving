def solution(edges):
  ans = [0, 0, 0, 0]
  n = max([max(i) for i in edges])
  checked = [False] * (n+1)
  indegrees = [[] for _ in range(n+1)]
  outdegrees = [[] for _ in range(n+1)]

  for edge in edges:
    a, b = edge
    checked[a] = True
    checked[b] = True
    outdegrees[a].append(b)
    indegrees[b].append(a)
  
  k = 0
  cnt = 0
  for i in range(1, n+1):
    if not checked[i]:
      continue
    if len(outdegrees[i]) >= 2 and len(indegrees[i]) == 0:
      k = i
      cnt = len(outdegrees[i])
      break
  for x in outdegrees[k]:
    indegrees[x].remove(k)
  
  ans[0] = k
  ### 일자 그래프 개수, indegree 0인 개수
  line_cnt = 0
  
  for i in range(1, n+1):
    if not checked[i]:
      continue
    if len(indegrees[i]) == 0 and i != k:
      line_cnt += 1
  ans[2] = line_cnt

  ### 팔자 그래프 개수, indegree 2, outdegree 2인 정점 개수
  eight_cnt = 0
  for i in range(1, n+1):
    if not checked[i]:
      continue
    if len(indegrees[i]) == 2 and len(outdegrees[i]) == 2:
      eight_cnt += 1

  ans[3] = eight_cnt
  ans[1] = cnt - line_cnt - eight_cnt

  return ans