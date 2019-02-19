#!/usr/bin/node
/* Getting file system object */
let fs = require('fs');

/* Setting up our variables */
let fp = process.argv[2];
let input = process.argv[3];

/* Writing to the file */
fs.writeFile(fp, input, function (err, data) {
  /* Prints out error if necessary */
  if (err) {
    console.log(err);
  }
});
