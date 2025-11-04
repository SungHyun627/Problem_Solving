const a = [3, 1, 2, 3, 4];
a.sort((a, b) => a - b);

const binary_search = (arr, target) => {
  let start = 0;
  let end = arr.length - 1;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    if (arr[mid] == target) return mid;
    if (arr[mid] > target) end = mid - 1;
    else start = mid + 1;
  }
  return -1;
};

console.log(a);
console.log(binary_search(a, 2));
