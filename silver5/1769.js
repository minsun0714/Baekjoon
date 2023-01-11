const input = require("fs").readFileSync("example.txt").toString().trim();
let word = String(input);
let count = 0;
while (word.length > 1) {
  word = String(word.split("").reduce((s, v) => s + Number(v), 0));
  count++;
}
console.log(count);
console.log(word % 3 === 0 ? "YES" : "NO");
