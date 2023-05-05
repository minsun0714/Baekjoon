let input = Number(require("fs").readFileSync("example.txt").toString().trim());

let dpTable = [...Array(input)].map((_) => 0);

for (let i = 2; i <= input; i++) {
  dpTable[i] = dpTable[i - 1] + 1;

  if (i % 2 === 0) {
    dpTable[i] = Math.min(dpTable[i], dpTable[parseInt(i / 2)] + 1);
  }
  if (i % 3 === 0) {
    dpTable[i] = Math.min(dpTable[i], dpTable[parseInt(i / 3)] + 1);
  }
}

console.log(dpTable[dpTable.length - 1]);
