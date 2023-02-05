const input = require("fs").readFileSync("example.txt").toString().trim();
const letters = input.split("").sort();
const freq = letters.reduce((acc, cur) => {
  acc[cur] ? acc[cur]++ : (acc[cur] = 1);
  return acc;
}, {});
let arr = [];
for (let v in freq) {
  arr.push(v.repeat(Math.floor(freq[v] / 2)));
}
let center = [];
for (let v in freq) {
  if (freq[v] % 2 !== 0) center.push(v);
}
const ans = [...arr, ...center.sort(), ...arr.reverse()].join("");
const L = ans.length;
const part1 = ans.substring(0, L / 2);
const part2 = L % 2 === 0 ? ans.substring(L / 2) : ans.substring(L / 2 + 1);

part1 === part2.split("").reverse().join("")
  ? console.log(ans)
  : console.log("I'm Sorry Hansoo");
