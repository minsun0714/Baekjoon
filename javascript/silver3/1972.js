const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.pop();
for (let str of input) console.log(`${str} is ${solution(str)}surprising.`);

function solution(str) {
  let ans = [];
  let count = 0;
  while (count < str.length) {
    let arr = [];
    count++;
    str.split("").forEach((letter, i, a) => {
      if (a[i + count] && !arr.includes(letter + a[i + count]))
        arr.push(letter + a[i + count]);
    });
    ans.push(arr.length);
  }
  return ans.reverse().every((v, i) => v === i) ? "" : "NOT ";
}
