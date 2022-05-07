const fs = require('fs');
const [nmv, ...edges] = fs
  .readFileSync('./input.txt')
  .toString()
  .trim()
  .split('\n');
const [n, m, v] = nmv.split(' ').map((i) => +i);

// 인접리스트
graph = new Array(n + 1).fill().map(() => []);

// 인접리스트 채우기
for (let edge of edges) {
  const [a, b] = edge.split(' ').map((i) => +i);
  graph[a].push(b);
  graph[b].push(a);
}

// 인접리스트 오름차순 정렬
for (let adj_node of graph) {
  adj_node.sort((a, b) => a - b);
}

const dfs_visited = Array(n + 1).fill(false);
const dfs_ans = [];

// DFS
function DFS(start) {
  dfs_visited[start] = true;
  dfs_ans.push(start);

  for (let node of graph[start]) {
    if (!dfs_visited[node]) DFS(node);
  }
}

// BFS
function BFS(start) {
  let ans = [];
  ans.push(start);
  let visited = Array(n + 1).fill(false);
  queue = [start];
  visited[start] = true;
  while (queue.length) {
    let next = queue.shift();
    for (let node of graph[next]) {
      if (!visited[node]) {
        visited[node] = true;
        ans.push(node);
        queue.push(node);
      }
    }
  }
  return ans;
}

DFS(v);
console.log(dfs_ans.join(' '));
console.log(BFS(v).join(' '));
