#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let str = '';
    for (let i = 0; i < this.width; ++i) {
      str += 'X';
    }
    for (let i = 0; i < this.height; ++i) {
      console.log(str);
    }
  }
  rotate () {
    let h = this.height;
    this.height = this.width;
    this.width = h;
  }
  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
