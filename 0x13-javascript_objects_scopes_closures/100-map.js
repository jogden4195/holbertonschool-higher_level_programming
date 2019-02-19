#!/usr/bin/node
let myList = require('./100-data').list;

let i = -1;
let newList = myList.map(x => x * ++i);

console.log(myList);
console.log(newList);
