let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
// testCase별로 나누기
input = input.map((v) => v.split(" "));
function testCases(input) {
  let testCases = [];
  while (input.length) {
    const set = Number(input[0][1]);
    testCases.push(input.splice(0, set + 1));
  }
  return testCases;
}

let bigArr = [];
for (let testCase of testCases(input)) {
  const J = Number(testCase[0][0]);
  testCase.shift();
  testCase = testCase.map(([R, C]) => +R * +C).sort((a, b) => b - a); // 내일차순으로 정렬

  let count = 0;
  let size = 0;
  let ans = [];
  testCase.forEach((v, i) => {
    size += v;
    if (size >= J) {
      count++;
      ans.push(i + 1);
      return;
    }
  });
  bigArr.push(ans);
}
ans = bigArr.map((v) => v[0]);
for (let v of ans) console.log(v);
