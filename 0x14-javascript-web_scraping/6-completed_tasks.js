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
      if (tasks[i]['completed'] === true) {
        let uid = tasks[i]['userId'].toString();
        if (Object.keys(workers).includes(uid) === false) {
          workers[uid] = 0;
        }
        let count = workers[uid];
        workers[uid] = ++count;
      }
    }
    console.log(workers);
  }
});
