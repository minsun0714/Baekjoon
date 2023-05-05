const num = require("fs").readFileSync("example.txt").toString().trim();

let arr = [];

for (let i = 0; i < num; i++) {
  arr.push("* ".repeat(i) + "*".repeat(4 * (num - i) - 3) + " *".repeat(i));
  if (i !== num - 1)
    arr.push(
      "* ".repeat(i + 1) + " ".repeat(4 * (num - i) - 7) + " *".repeat(i + 1)
    );
}
for (let line of arr) console.log(line);
for (let line of arr.reverse().slice(1)) console.log(line);
