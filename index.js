const inputFileName =
  process.platform === "linux" ? "/dev/stdin" : "example.txt";

const input = require("fs")
  .readFileSync(inputFileName)
  .toString()
  .trim()
  .split("\n");
