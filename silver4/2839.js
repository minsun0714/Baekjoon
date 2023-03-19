let input = Number(require("fs").readFileSync("example.txt").toString().trim());

let dpTable = [0];

for (let i = 1; i <= input; i++) {
  if (i === 3 || i === 5) {
    dpTable[i] = 1;
    continue;
  }
  if (i - 5 < 0 || i - 3 < 0) {
    dpTable[i] = -1;
    continue;
  }
  if (dpTable[i - 5] !== -1) {
    dpTable[i] = dpTable[i - 5] + 1;
    continue;
  } else if (dpTable[i - 3] !== -1) {
    dpTable[i] = dpTable[i - 3] + 1;
    continue;
  } else {
    dpTable[i] = -1;
  }
}

console.log(dpTable[dpTable.length - 1]);
