const input = require("fs").readFileSync("example.txt").toString().trim();
const alp = input[0];
const plusMinus = input[1];

const grade = {
  A: 4,
  B: 3,
  C: 2,
  D: 1,
  F: 0,
};

if (plusMinus === "+") {
  grade[alp] += 0.3;
} else if (plusMinus === "-") {
  grade[alp] -= 0.3;
} else {
  grade[alp] = grade[alp].toFixed(1);
}

console.log(grade[alp]);
