const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((v) =>
    v
      .split(" ")
      .map((w) => Number(w))
      .reduce((s, w) => (s += w), 0)
  );
input.shift();
for (let v of input) console.log(v);
