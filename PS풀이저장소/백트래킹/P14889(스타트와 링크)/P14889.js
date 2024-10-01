// P14889 스타트와 링크
const fs = require('fs');
const input = fs.readFileSync('./input.txt').toString().trim().split('\n');
const n = +input.shift();
const arr = new Array(n).fill(0).map(() => new Array(n).fill(0));
let start_sum = 0;
let link_sum = 0;
let min_diff = 20 * 20 * 100;
const in_team = new Array(n).fill(false);
const start_team = [];

for (let i = 0; i < n; i++) {
  arr[i] = input
    .shift()
    .split(' ')
    .map((x) => +x);
}

function backtracking(num, t) {
  if (num === parseInt(n / 2)) {
    for (let i = 0; i < n; i++) {
      if (!in_team[i]) {
        for (let j = 0; j < n; j++) {
          if (i === j) continue;
          if (!in_team[j]) {
            link_sum += arr[i][j];
          }
        }
      }
    }
    diff = Math.abs(start_sum - link_sum);
    if (min_diff > diff) min_diff = diff;
    link_sum = 0;
    return;
  }

  for (let i = t + 1; i < n; i++) {
    if (!in_team[i]) {
      for (let j of start_team) {
        start_sum += arr[i][j];
        start_sum += arr[j][i];
      }
      in_team[i] = true;
      start_team.push(i);
      backtracking(num + 1, i);
      in_team[i] = false;
      start_team.pop();

      for (let j of start_team) {
        start_sum -= arr[i][j];
        start_sum -= arr[j][i];
      }
    }
  }
}
backtracking(0, -1);
console.log(min_diff);
