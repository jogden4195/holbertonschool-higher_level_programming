#!/usr/bin/node
/* Creating request object */
const request = require('request');

/* Sending GET request for wanted url */
let ep = parseInt(process.argv[2]);
let swapi = 'http://swapi.co/api/films/';
request(swapi, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let films = JSON.parse(body).results;
    let found = false;
    for (let i in films) {
      if (films[i]['episode_id'] === ep) {
        console.log(films[i]['title']);
        found = true;
      }
    }
    if (found === false) {
      console.log('undefined');
    }
  }
});
