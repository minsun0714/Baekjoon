const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(" ");
const [num0, num1] = [+input[0], +input[1]];
for (let i = num0; i <= num1; i++) {
  isPrime(i) ? console.log(i) : null;
}
function isPrime(n) {
  if (n < 2) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}
