let input = require("fs").readFileSync("example.txt").toString().trim();
let ans = [];
for (let i = 0; i < input.length; i++) {
  for (let j = i + 1; j <= input.length; j++) {
    ans.push(input.substring(i, j));
  }
}
console.log([...new Set(ans)].length);
