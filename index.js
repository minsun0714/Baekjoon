const input = require("fs").readFileSync("example.txt").toString().trim();
const arr = input.split("\n").map((v) => v.split(" "));
const res = arr.map((v) => v.map((w) => Number(w)));
res.shift();
const ans = res.map(
  (v, i) =>
    "Case #" +
    (Number(i) + 1) +
    ": " +
    v[0] +
    " + " +
    v[1] +
    " = " +
    v.reduce((s, w) => (s += w), 0)
);
for (let v of ans) console.log(v);
