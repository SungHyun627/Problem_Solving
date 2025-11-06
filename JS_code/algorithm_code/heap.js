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

  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }

  heappush(value) {
    this.heap.push(value);
    this.bubbleUp();
  }

  heappop() {
    if (this.size() === 0) return undefined;
    if (this.size() === 1) return this.heap.pop();

    const value = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown();
    return value;
  }

  bubbleUp() {
    let idx = this.size() - 1;
    while (idx > 0) {
      const parent = Math.floor((idx - 1) / 2);
      if (this.heap[parent] <= this.heap[idx]) break;
      this.swap(idx, parent);
      idx = parent;
    }
  }

  bubbleDown() {
    let idx = 0;
    while (true) {
      const left = idx * 2 + 1;
      const right = idx * 2 + 2;
      let smallest = idx;

      if (left < this.size() && this.heap[left] < this.heap[smallest]) smallest = left;
      if (right < this.size() && this.heap[right] < this.heap[smallest]) smallest = right;
      if (smallest === idx) break;

      this.swap(idx, smallest);
      idx = smallest;
    }
  }
}

const h = new Heap();
console.log(h.heappush(2));
console.log(h.heappush(3));
console.log(h.heappush(100));
console.log(h.heappush(5));
console.log(h.heappop());
console.log(h.heappop());
console.log(h.get());
