const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((r) => r.split(" ").map(Number));
const [A, B] = input[0];
input.shift();
input.shift();
let favorites = input.flat().sort((a, b) => a - b);
favorites = favorites.map((favorite) => Math.abs(favorite - B));
const shortestFavorite = Math.min(...favorites) + 1;
const direct = Math.abs(A - B);
console.log(Math.min(shortestFavorite, direct));
