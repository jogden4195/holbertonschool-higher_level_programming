#!/usr/bin/node
let myList = require('./100-data').list;

let newList = myList.map(x => x * myList.indexOf(x));

console.log(myList);
console.log(newList);
