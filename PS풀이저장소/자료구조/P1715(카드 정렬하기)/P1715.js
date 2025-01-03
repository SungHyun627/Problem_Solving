class Heap {
  constructor() {
    this.heap = [];
  }

  get() {
    return [...this.heap];
  }

  size() {
    return this.heap.length;
  }

  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }

  heappush(value) {
    this.heap.push(value);
    this.bubbleUp();
  }

  heappop() {
    if (this.heap.length === 0) {
      return null;
    }

    if (this.heap.length === 1) {
      return this.heap.pop();
    }

    const value = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown();
    return value;
  }

  bubbleUp() {
    let curIdx = this.heap.length - 1;
    //부모 인덱스
    let parentIdx = Math.floor((curIdx - 1) / 2);

    // 부모 값이 존재하고, 부모 값보다 현재값이 더 작은 경우 swap
    while (curIdx > 0 && this.heap[curIdx] < this.heap[parentIdx]) {
      this.swap(curIdx, parentIdx);
      curIdx = parentIdx;
      parentIdx = Math.floor((curIdx - 1) / 2);
    }
  }

  bubbleDown() {
    let curIdx = 0;
    let leftIdx = curIdx * 2 + 1;
    let rightIdx = curIdx * 2 + 2;

    while (
      (this.heap[leftIdx] && this.heap[leftIdx] < this.heap[curIdx]) ||
      (this.heap[rightIdx] && this.heap[rightIdx] < this.heap[curIdx])
    ) {
      let smallerIdx = leftIdx;

      if (this.heap[rightIdx] && this.heap[rightIdx] < this.heap[smallerIdx]) {
        smallerIdx = rightIdx;
      }

      this.swap(curIdx, smallerIdx);
      curIdx = smallerIdx;
      leftIdx = curIdx * 2 + 1;
      rightIdx = curIdx * 2 + 2;
    }
  }
}

const h = new Heap();
const fs = require('fs');
const input = fs.readFileSync('./input.txt').toString().trim().split('\n');
const n = +input.shift();
const arr = [];
let result = 0;

for (let i = 0; i < n; i++) {
  h.heappush(+input.shift());
}

if (h.size() !== 1) {
  while (true) {
    let x = h.heappop();
    let y = h.heappop();
    result += x + y;

    if (h.size() === 0) break;
    h.heappush(x + y);
  }
}

console.log(result);
