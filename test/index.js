const date = new Date();
const year = date.getFullYear();
const month = date.getMonth() + 1;
const monthPad = String(month).padStart(2, "0");
const todaysdate = String(date.getDate()).padStart(2, "0");
console.log(`${year}-${monthPad}-${todaysdate}`);
