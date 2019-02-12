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
    if (parseInt(process.argv[i]) > biggest) {
      secBig = biggest;
      biggest = process.argv[i];
    }
    ++i;
  }
  console.log(secBig);
}
