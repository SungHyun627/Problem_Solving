const fs = require('fs');
const input = fs.readFileSync('./input.txt').toString().trim().split('\n');
t = +input.shift();

const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];

function solution(params) {
  const [m, n, k] = params;
  const graph = new Array(n).fill(0).map(() => new Array(m).fill(0));
  const visited = new Array(n).fill(0).map(() => new Array(m).fill(false));
  const queue = [];
  let result = 0;

  for (let i = 0; i < k; i++) {
    temp = input
      .shift()
      .split(' ')
      .map((el) => parseInt(el));
    graph[temp[1]][temp[0]] = 1;
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (graph[i][j] && !visited[i][j]) {
        queue.push([i, j]);
        visited[i][j] = true;
        while (queue.length) {
          [x, y] = queue.shift();
          for (let d = 0; d < 4; d++) {
            let nx = x + dx[d];
            let ny = y + dy[d];
            if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
            if (!visited[nx][ny] && graph[nx][ny]) {
              queue.push([nx, ny]);
              visited[nx][ny] = true;
            }
          }
        }
        result += 1;
      }
    }
  }
  return result;
}

for (let i = 0; i < t; i++) {
  console.log(
    solution(
      input
        .shift()
        .split(' ')
        .map((el) => +el)
    )
  );
}
