const input = require("fs").readFileSync("example.txt").toString().trim();
const n = Number(input);
let cards = [...Array(n)].map((_, i) => i + 1);
let discard = [];
while (cards.length > 1) {
  discard.push(cards[0]);
  cards.shift();
  cards.push(cards[0]);
  cards.shift();
}
const ans = [...discard, ...cards].join(" ");
console.log(ans);
