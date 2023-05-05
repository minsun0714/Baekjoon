let input = require("fs").readFileSync("example.txt").toString().trim();

let sum = 0;
let num = 0;
while (sum <= Number(input)) {
  num++;
  sum += num;
}
console.log(num - 1);
