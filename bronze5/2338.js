const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const [A, B] = [BigInt(input[0]), BigInt(input[1])];
console.log((A + B).toString());
console.log((A - B).toString());
console.log((A * B).toString());
