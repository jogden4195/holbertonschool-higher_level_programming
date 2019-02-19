#!/usr/bin/node
/* Creating request object */
const request = require('request');

/* Sending GET request for wanted url */
let url = process.argv[2];
request(url, function (err, res, body) {
  if (err || res) {
    console.log('code: ' + res.statusCode);
  }
});
