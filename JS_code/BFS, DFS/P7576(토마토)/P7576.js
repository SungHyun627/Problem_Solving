// P7576. 토마토
const fs = require('fs');
const input = fs.readFileSync('./input.txt').toString().trim().split('\n');

class Deque {
  constructor() {
    this.queue = [];
    this.head = 0;
  }

  push(el) {
    this.queue.push(el);
  }

  popleft() {
    return this.queue[this.head++];
  }

  isEmpty() {
    return this.head >= this.queue.length;
  }
}

const [m, n] = input
  .shift()
  .split(' ')
  .map((el) => +el);

const board = new Array(n).fill(0);
let res = -1;
const dx = [0, 0, -1, 1];
const dy = [-1, 1, 0, 0];
let wall_cnt = 0;
let ripen_cnt = 0;

for (let i = 0; i < n; i++) {
  board[i] = input
    .shift()
    .split(' ')
    .map((el) => +el);
}

const q = new Deque();

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (board[i][j] === 1) {
      q.push([i, j, 0]);
      ripen_cnt += 1;
      continue;
    }
    if (board[i][j] == -1) {
      wall_cnt += 1;
    }
  }
}

while (!q.isEmpty()) {
  const [x, y, cnt] = q.popleft();
  res = cnt;

  for (let k = 0; k < 4; k++) {
    let nx = x + dx[k];
    let ny = y + dy[k];

    if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
    if (board[nx][ny] !== 0) continue;

    board[nx][ny] = 1;
    ripen_cnt += 1;
    q.push([nx, ny, cnt + 1]);
  }
}

console.log(ripen_cnt + wall_cnt === n * m ? res : -1);
