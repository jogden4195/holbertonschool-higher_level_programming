#!/usr/bin/node
const oldSquare = require('./5-square');
module.exports = class Square extends oldSquare {
  charPrint (c) {
    let character;
    let str = '';
    if (c) {
      character = c;
    } else {
      character = 'X';
    }
    for (let i = 0; i < this.width; ++i) {
      str += character;
    }
    for (let i = 0; i < this.width; ++i) {
      console.log(str);
    }
  }
};
