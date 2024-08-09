const m = new Map();

m.set(1, [2, 3, 4]);
m.set('dfdsf', [234]);
console.log(m.get(1));

for (let x of m.keys()) {
  console.log(x);
}

const a = [...m];
console.log(a);

const k = [1, 2, 3, 4];
console.log(k.sort((a, b) => b - a));

const m2 = a.reduce((acc, cur) => acc.set(cur[0], cur[1]), new Map());
console.log(m2);

for (let [key, value] of m2) {
  console.log(key, value);
}

const s1 = new Set();
s1.add(2);
s1.add([2, 3, 4]);
s1.delete(2);

for (let [key, value] of s1) {
  console.log(key, value);
}
