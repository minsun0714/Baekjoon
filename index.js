const inputFileName =
  process.platform === "linux" ? "/dev/stdin" : "example.txt";

const input = require("fs")
  .readFileSync(inputFileName)
  .toString()
  .trim()
  .split("\n")
  .map((r) => r.split(" ").map(Number));
const [[N, K], ...items] = input;
