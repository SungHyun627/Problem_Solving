const arr1 = [1, 2, 3, 4, 5, 6, 7];
const n = arr1.length;
const target = 4;

const binarySearch = (arr, target, start, end) => {
  while (start <= end) {
    mid = parseInt((start + end) / 2);
    if (arr[mid] === target) return mid;
    if (arr[mid] > target) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
};
