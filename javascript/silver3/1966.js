const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" "));
input.shift();

while (input.length) {
  console.log(solution(input.splice(0, 2)));
}

function solution(testCase) {
  let [targetIdx, queue] = [testCase[0][1], testCase[1]];

  let objQueue = [];
  queue.forEach((v, i) => {
    objQueue.push({ isTarget: i === +targetIdx, value: v });
  });

  let count = 0;
  while (true) {
    const first = objQueue.splice(0, 1)[0];
    if (objQueue.some((v) => v.value > first.value)) objQueue.push(first);
    else {
      count++;
      if (first.isTarget) return count;
    }
  }
}
