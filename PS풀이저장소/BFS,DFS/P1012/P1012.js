const fs = require('fs');
const input = fs.readFileSync('./input.txt').toString().trim().split('\n');
t = +input.shift();

const dx = [0, 0, -1, 1];
const dy = [-1, 1, 0, 0];

function solution(n, m, arr) {
  let result = 0;

  const vis = new Array(n).fill(0).map(() => new Array(m).fill(false));
  const graph = new Array(n).fill(0).map(() => new Array(m).fill(0));
  const q = [];

  for (let [b, a] of arr) {
    graph[a][b] = 1;
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      // 방문했거나 배추가 아닌 경우
      if (vis[i][j] || graph[i][j] === 0) continue;
      vis[i][j] = true;
      q.push([i, j]);

      while (q.length !== 0) {
        const [x, y] = q.shift();
        for (k = 0; k < 4; k++) {
          let nx = x + dx[k];
          let ny = y + dy[k];

          // 벗어났을 때
          if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
          // 방문기록이 있거나 배추가 아닐 때
          if (vis[nx][ny] || graph[nx][ny] === 0) continue;

          q.push([nx, ny]);
          vis[nx][ny] = true;
        }
      }
      result += 1;
    }
  }

  return result;
}

for (let i = 0; i < t; i++) {
  const [m, n, k] = input
    .shift()
    .split(' ')
    .map((x) => +x);

  b = [];

  for (j = 0; j < k; j++) {
    b.push(
      input
        .shift()
        .split(' ')
        .map((x) => +x)
    );
  }
  console.log(solution(n, m, b));
}
