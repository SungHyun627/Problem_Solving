// 순열, 조합

const getCombination = (arr, n) => {
  if (n === 1) return arr.map((el) => el);
  const result = [];

  arr.forEach((fixed, idx, origin) => {
    const rest = origin.slice(idx + 1);
    const combis = getCombination(rest, n - 1);
    const attached = combis.map((combi) => {
      if (n === 2) return [fixed, combi];
      return [fixed, ...combi];
    });
    result.push(...attached);
  });

  return result;
};

const getPermutation = (arr, n) => {
  if (n === 1) return arr.map((el) => el);
  const result = [];

  arr.forEach((fixed, idx, origin) => {
    const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)];
    const perms = getPermutation(rest, n - 1);
    const attached = perms.map((perm) => {
      if (n === 2) return [fixed, perm];
      return [fixed, ...perm];
    });
    result.push(...attached);
  });

  return result;
};

const arr = [1, 2, 3, 4];

console.log(getCombination(arr, 2));
console.log(getPermutation(arr, 2));
