const fs = require('fs');
const input = fs.readFileSync('./input.txt').toString().trim().split('\n');
const [n, e, v] = input
  .shift()
  .split(' ')
  .map((x) => +x);

const graph = new Array(n + 1).fill(0).map(() => new Array());
let vis = new Array(n + 1).fill(false);
let result = [];

for (let i = 0; i < e; i++) {
  const [x, y] = input
    .shift()
    .split(' ')
    .map((x) => +x);
  graph[x].push(y);
  graph[y].push(x);
}

for (let i = 1; i < n + 1; i++) {
  graph[i].sort((a, b) => a - b);
}

const dfs = (node) => {
  result.push(node);
  for (let v of graph[node]) {
    if (vis[v]) continue;
    vis[v] = true;
    dfs(v);
  }
};

const bfs = (s) => {
  const q = [];
  q.push(s);
  result.push(s);
  vis[s] = true;

  while (q.length !== 0) {
    x = q.shift();

    for (let v of graph[x]) {
      if (vis[v]) continue;
      result.push(v);
      vis[v] = true;
      q.push(v);
    }
  }
};

vis[v] = true;
dfs(v);
console.log(result.join(' '));
result = [];
vis = new Array(n + 1).fill(false);
bfs(v);
console.log(result.join(' '));

export const api = async () => {
  try {
    const res = await fetch(`apiurl`);
    if (!res.ok) throw new Error('에러 발생');
    return;
  } catch (e) {}
};

sdsdsdsddddsdsddsdsssaddadqwdassdsdwdq  1211211212123213123qwassaasasaㅇㄴㅇㄴㅁㅇㄴ    