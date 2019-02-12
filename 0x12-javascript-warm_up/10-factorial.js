#!/usr/bin/node
function factorial (n) {
  let num = parseInt(n);
  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
} 
if (parseInt(process.argv[2])) {
  console.log(factorial(process.argv[2]));
} else {
  console.log(1);
}
