#!/usr/bin/node
/* Getting file system object */
let fs = require('fs');

/* Reading file */
let fp = process.argv[2];
fs.readFile(fp, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
