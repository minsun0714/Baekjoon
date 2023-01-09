const input = require("fs").readFileSync("/dev/stdin").toString().split("");
let arr = [];
for (let v of input)
  v === v.toUpperCase() ? arr.push(v.toLowerCase()) : arr.push(v.toUpperCase());
console.log(arr.join(""));
