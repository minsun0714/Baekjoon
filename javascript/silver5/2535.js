const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
const data = input.map((v) => v.split(" "));
data.sort((a, b) => b[2] - a[2]);
let arr = ([gold, silver] = [data[0], data[1]]);
if (gold[0] !== silver[0]) {
  arr.push(data[2]);
} else {
  while (data[0][0] === gold[0]) {
    data.shift();
  }
  data.sort((a, b) => b[2] - a[2]);
  arr.push(data[0]);
}
for (let v of arr) console.log(v[0] + " " + v[1]);
