// P12865. 평범한 배낭
const fs = require('fs');
const input = fs.readFileSync('./input.txt').toString().trim().split('\n');

const [n, k] = input
  .shift()
  .split(' ')
  .map((el) => +el);
const weights = new Array(n).fill(0);
const values = new Array(n).fill(0);
const dp = new Array(k + 1).fill(0);

for (let i = 0; i < n; i++) {
  const [w, v] = input
    .shift()
    .split(' ')
    .map((el) => +el);
  weights[i] = w;
  values[i] = v;
}

for (let i = 0; i < n; i++) {
  const w = weights[i];
  const v = values[i];

  for (let j = k; j >= w; j--) {
    dp[j] = Math.max(dp[j], dp[j - w] + v);
  }
}

console.log(dp[k]);
