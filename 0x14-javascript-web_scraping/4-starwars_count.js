#!/usr/bin/node
/* Creating request object */
const request = require('request');

/* Sending GET request for wanted url */
let swapi = process.argv[2];
request(swapi, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let films = JSON.parse(body).results;
    let count = 0;
    let wedge = 'https://swapi.co/api/people/18/';
    for (let i in films) {
      if (films[i]['characters'].includes(wedge) === true) {
        ++count;
      }
    }
    console.log(count);
  }
});
