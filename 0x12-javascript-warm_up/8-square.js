#!/usr/bin/node
if (parseInt(process.argv[2])) {
  let i;
  let end = parseInt(process.argv[2]);
  let str = '';
  for (i = 0; i < end; ++i) {
    str += 'X';
  }
  for (i = 0; i < end; ++i) {
    console.log(str);
  }
} else {
  console.log('Missing size');
}
