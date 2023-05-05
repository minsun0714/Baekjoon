let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
input = input.filter((v) => isNaN(+v)).map((v) => v.split(" "));
for (let testCase of input) console.log(solution(testCase));

function solution(testCase) {
  let ans = "";
  testCase.forEach((card) => {
    ans[0]?.localeCompare(card) < 0 ? (ans += card) : (ans = card + ans);
  });
  return ans;
}
