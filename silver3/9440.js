let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map(Number));
input.pop();
input.forEach((testCase) =>
  console.log(solution(testCase.slice(1).sort((a, b) => a - b)))
);

function solution(testCase) {
  let arr1 = [];
  let arr2 = [];
  testCase.forEach((n, i, a) => {
    if (arr1.length === 0 && n === 0) {
      arr1.push(a.find((v) => v !== 0));
      a.splice(a.indexOf(arr1[arr1.length - 1]), 1, "?");
    }
    if (arr2.length === 0 && n === 0) {
      arr2.push(a.find((v) => v !== 0 && !isNaN(v)));
      a.splice(a.indexOf(arr2[arr2.length - 1]), 1, "?");
    }
    i % 2 === 0 ? arr1.push(n) : arr2.push(n);
  });
  const num1 = arr1.filter((n) => !isNaN(n)).join("");
  const num2 = arr2.filter((n) => !isNaN(n)).join("");
  return Number(num1) + Number(num2);
}
