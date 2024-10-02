const fs = require('fs');
const input = fs.readFileSync('./input.txt').toString().trim().split('\n');

const [n, m] = input
  .shift()
  .split(' ')
  .map((x) => +x);
const graph = new Array(n + 1).fill(0).map(() => new Array(n + 1).fill(Infinity));
let minSum = Infinity;
let answer = 0;

for (let i = 0; i < m; i++) {
  const [x, y] = input
    .shift()
    .split(' ')
    .map((x) => +x);
  graph[x][y] = 1;
  graph[y][x] = 1;
}

for (let k = 1; k < n + 1; k++) {
  for (let i = 1; i < n + 1; i++) {
    for (let j = 1; j < n + 1; j++) {
      graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
    }
  }
}

for (let i = 1; i < n + 1; i++) {
  const baconSum = graph[i].slice(1).reduce((a, b) => a + b, 0);
  if (baconSum < minSum) {
    minSum = baconSum;
    answer = i;
  }
}
console.log(answer);
