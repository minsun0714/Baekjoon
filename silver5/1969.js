const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
const length = input[0].split(" ")[1];
input.shift();

let wholeArray = [];
for (let i = 0; i < length; i++) {
  let arr = [];
  for (let j = 0; j < input.length; j++) {
    arr.push(input[j][i]);
  }
  wholeArray.push(arr);
}

let frqArr = [];
for (let v of wholeArray) frqArr.push(frq(v));
let array = [];
for (let v of frqArr) {
  let smallArray = [];
  for (let w in v) {
    smallArray.push([w, v[w]]);
  }
  array.push(smallArray);
}
let most = [];
for (let v of array) most.push(v.sort().sort((a, b) => b[1] - a[1])[0]);
const answer = most.map((v) => v[0]).join("");
console.log(answer);

let H = [];
for (let v of input) H.push(v.split("").filter((v, i) => v !== answer[i]));
console.log(H.flat().length);

function frq(a) {
  return a.reduce((acc, cur) => {
    acc[cur] ? acc[cur]++ : (acc[cur] = 1);
    return acc;
  }, {});
}
