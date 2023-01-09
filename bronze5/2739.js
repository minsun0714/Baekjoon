const input = require("fs").readFileSync("example.txt").toString();
let num = Number(input[0]);
for (let i = 1; i <= 9; i++) {
  console.log(num + " * " + i + " = " + num * i);
}
