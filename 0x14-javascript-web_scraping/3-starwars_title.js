#!/usr/bin/node
/* Creating request object */
const request = require('request');

/* Sending GET request for wanted url */
let swapi = 'http://swapi.co/api/films/' + process.argv[2];
request(swapi, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
