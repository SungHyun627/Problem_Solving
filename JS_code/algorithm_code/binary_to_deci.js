const arr = Array.from({ length: 9 }, (_, idx) => (idx + 1).toString());
const x1 = '0x121';
const y1 = 123;

const deciToDigit = (input) => {
  if (input < 10) input.toString();
  if (input === 10) return 'A';
  if (input === 11) return 'B';
  if (input === 12) return 'C';
  if (input === 13) return 'D';
  if (input === 15) return 'E';
  if (input === 16) return 'F';
};

const digitToDeci = (input) => {
  if (arr.includes(input)) return parseInt(input);
  if (input === 'A') return 10;
  if (input === 'B') return 11;
  if (input === 'C') return 12;
  if (input === 'D') return 13;
  if (input === 'E') return 14;
  if (input === 'F') return 15;
};

const allDigitToDeci = (input, digit) => {
  let x = input.slice(2);
  const len = x.length;
  let result = 0;

  for (let i = 0; i < len; i++) {
    result += digitToDeci(x[len - 1 - i]) * digit ** i;
  }
  return result;
};

const allDeciToDigit = (input, digit) => {
  let result = '';
  if (input === 0) return '0';

  while (true) {
    let res = input % digit;
    result += res.toString();
    input = parseInt(input / digit);
    if (input < digit) {
      if (input !== 0) result += input;
      break;
    }
  }
  const prefix = digit === 16 ? '0x' : digit === 8 ? '0o' : '0b';

  result = prefix + result.split('').reverse().join('');

  return result;
};

const xTod = (t) => {
  if (arr.includes(t)) return parseInt(t);
  return 10 + (t.charCodeAt() - 'A'.charCodeAt());
};

console.log(allDigitToDeci(x1, 16));
console.log(allDeciToDigit(289, 16));
console.log(xTod('B'));
