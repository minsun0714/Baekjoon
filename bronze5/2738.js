const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const nm = input[0].split(" ");
const arr1 = input.splice(1, nm[0]).map((v) => v.split(" "));
const arr2 = input.splice(1, nm[0]).map((v) => v.split(" "));
const ans = arr1.map((v, i) =>
  v.map((w, j) => Number(w) + Number(arr2[i][j])).join(" ")
);
for (let v of ans) console.log(v);
