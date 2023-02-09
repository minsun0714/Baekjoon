const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
console.log(solution(input));
function solution(input) {
  let arr = [];
  const double = input.map((word) => word + word);
  input.forEach((v, i) => {
    arr.push(double.find((d) => d.length / 2 === v.length && d.includes(v)));
  });
  return [...new Set(arr)].length;
}
