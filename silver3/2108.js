const inputFileName =
  process.platform === "linux" ? "/dev/stdin" : "example.txt";
const input = require("fs")
  .readFileSync(inputFileName)
  .toString()
  .trim()
  .split("\n");
const [N, ...arr] = input.map(Number);
arr.sort((a, b) => a - b);

const sum = arr.reduce((s, v) => s + v);
const A = Math.round(sum / N);

const midIndex = Math.floor(N / 2);
const B = arr[midIndex];

const freq = Object.entries(
  arr.reduce((acc, cur) => {
    acc[cur] ? acc[cur]++ : (acc[cur] = 1);
    return acc;
  }, {})
).sort((a, b) => b[1] - a[1]);

const mostFreq = freq[0][1];
const mostFreqs = freq.filter((fr) => fr[1] === mostFreq);
mostFreqs.sort((a, b) => a[0] - b[0]);
const C = mostFreqs.length > 1 ? +mostFreqs[1][0] : +mostFreqs[0][0];

const D = arr.pop() - arr.shift();

function print(num) {
  num ? console.log(num) : console.log(0);
}
print(A);
print(B);
print(C);
print(D);
