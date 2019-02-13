#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let biggest;
  let secBig;
  if (parseInt(process.argv[2]) >= parseInt(process.argv[3])) {
    biggest = parseInt(process.argv[2]);
    secBig = parseInt(process.argv[3]);
  } else {
    biggest = parseInt(process.argv[3]);
    secBig = parseInt(process.argv[2]);
  }
  let i = 4;
  while (i < process.argv.length) {
    let current = parseInt(process.argv[i]);
    if (current > biggest) {
      secBig = biggest;
      biggest = current;
    } else if (current < biggest && current > secBig) {
      secBig = current;
    }
    ++i;
  }
  console.log(secBig);
}
