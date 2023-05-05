let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");

const [A, B] = [input[0], input[1]];
const [lengthA, lengthB] = [A.length, B.length];

function fnGCD(x, y) {
  return x % y ? fnGCD(y, x % y) : y;
}

const LCM = (lengthA * lengthB) / fnGCD(lengthA, lengthB);
const repeatedA = A.repeat(LCM / lengthA);
const repeatedB = B.repeat(LCM / lengthB);
repeatedA === repeatedB ? console.log(1) : console.log(0);
