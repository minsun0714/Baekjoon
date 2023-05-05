let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(" ");
const [A, B] = input.map(Number);
let ans = 0;
function solution(A, B, count = 0) {
  if (A <= B) {
    count++;
    if (!isNaN(solution(2 * A, B, count))) ans += solution(2 * A, B, count);
    if (!isNaN(solution(Number(String(A) + "1"), B, count)))
      ans += solution(Number(String(A) + "1"), B, count);
  }
  if (A === B) return count;
}
solution(A, B);
ans ? console.log(ans) : console.log(-1);
