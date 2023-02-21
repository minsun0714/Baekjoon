let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
while (input.length > 0) {
  console.log(minDif(input.splice(0, 2)[1].split(" ").map(Number)));
}

function minDif(arr) {
  arr.sort((a, b) => a - b);
  let odd = [];
  let even = [];
  arr.forEach((v, i, a) => {
    i % 2 === 0 ? odd.push(v) : even.push(v);
  });
  arr = [...odd.concat(even.reverse()), arr[0]];
  return Math.max(
    ...arr.map((v, i, a) => Math.abs(v - a[i + 1])).slice(0, arr.length - 1)
  );
}
