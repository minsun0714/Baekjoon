const input = require("fs").readFileSync("example.txt").toString().trim();
const N = Number(input);
let count = 0;
for (let i = 1; ; i++) {
  const num = String(i);

  if (!num.includes("666")) continue;
  count++;
  if (count === N) {
    console.log(num);
    break;
  }
}
