const input = require("fs").readFileSync("example.txt").toString().trim();
const roomN = input.split("");
const from9to6 = roomN.map((v) => (v === "9" ? "6" : v));
const freq = from9to6.reduce((acc, cur) => {
  acc[cur] ? acc[cur]++ : (acc[cur] = 1);
  return acc;
}, {});

freq[6] = freq[6] ? Math.ceil(freq[6] / 2) : 0;

let arr = [];
for (let v in freq) arr.push([v, freq[v]]);

arr.sort((a, b) => b[1] - a[1]);
console.log(arr[0][1]);
