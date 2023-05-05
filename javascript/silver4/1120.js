const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(" ");
const [W1, W2] = [input[0], input[1]];
const [L1, L2] = [W1.length, W2.length];
const lengthDif = L2 - L1;
let dif = [];
if (L1 === L2) {
  input[0].split("").forEach((v, i) => {
    v !== W2[i] ? dif.push(v) : null;
  });
  console.log(dif.length);
} else {
  for (let i = 0; i <= lengthDif; i++) {
    dif.push(
      (
        W2.substring(0, i) +
        W1 +
        W2.split("")
          .slice(lengthDif * -1 + i)
          .join("")
      ).substring(0, L2)
    );
  }
  let ans = [];
  for (let v of dif) {
    ans.push(compare(v, W2));
  }
  console.log(Math.min(...ans));
}

function compare(v, W2) {
  let dif = [];
  const str1 = v.split("");
  const str2 = W2.split("");
  str1.forEach((v, i) => (v !== str2[i] ? dif.push(v) : null));
  return dif.length;
}
