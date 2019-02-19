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
    for (let i in films) {
      for (let j in films[i]['characters']) {
        if (films[i]['characters'][j].includes('18/') === true) {
          ++count;
        }
      }
    }
    console.log(count);
  }
});
