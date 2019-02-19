#!/usr/bin/node
/* Creating request and fs objects */
const request = require('request');
const fs = require('fs');

/* Sending GET request for wanted url */
let url = process.argv[2];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let fp = process.argv[3];
    fs.writeFile(fp, body, function (err, data) {
      /* Prints out error if necessary */
      if (err) {
        console.log(err);
      }
    });
  }
});
