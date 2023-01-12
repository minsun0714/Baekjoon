const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");

let word = String(input);
word = word.replace(/c=/g, "_");
word = word.replace(/c-/g, "_");
word = word.replace(/dz=/g, "_");
word = word.replace(/d-/g, "_");
word = word.replace(/lj/g, "_");
word = word.replace(/nj/g, "_");
word = word.replace(/s=/g, "_");
word = word.replace(/z=/g, "_");
console.log(word.split("").length);
