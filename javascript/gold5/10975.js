let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
const slicedAndSorted = input.slice().sort((a, b) => a - b);
let ans = [];
input.forEach((v, i) => {
  if (i === 0) {
    ans.push([v]);
    return;
  }
  let count = 0;
  for (let i = 0; i < ans.length; i++) {
    const first = ans[i][0];
    const last = ans[i][ans[i].length - 1];

    const gap1 = slicedAndSorted.indexOf(first) - slicedAndSorted.indexOf(v);
    const gap2 = slicedAndSorted.indexOf(v) - slicedAndSorted.indexOf(last);

    if (gap1 === 1) {
      ans[i].unshift(v);
      count++;
      return;
    } else if (gap2 === 1) {
      ans[i].push(v);
      count++;
      return;
    }
  }
  if (!count) ans.push([v]);
});
console.log(ans.length);
