const input = require("fs").readFileSync("example.txt").toString().trim();
const one = input.split("0").filter((v) => v);
const zero = input.split("1").filter((v) => v);
console.log(Math.min(one.length, zero.length));
