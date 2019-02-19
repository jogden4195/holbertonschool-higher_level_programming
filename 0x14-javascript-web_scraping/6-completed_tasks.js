#!/usr/bin/node
/* Creating request object */
const request = require('request');

/* Sending GET request for wanted url */
let url = process.argv[2];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let tasks = JSON.parse(body);
    let workers = {};
    for (let i in tasks) {
      let uid = tasks[i]['userId'];
      if (Object.keys(workers).includes(uid.toString()) === false) {
        workers[uid] = 0;
      }
      if (tasks[i]['completed'] === true) {
        let count = workers[uid];
        workers[uid] = ++count;
      }
    }
    console.log(workers);
  }
});
