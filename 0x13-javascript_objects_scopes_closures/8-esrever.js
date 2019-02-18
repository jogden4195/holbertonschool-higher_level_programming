#!/usr/bin/node
exports.esrever = function (list) {
  let newArray = [];
  let len = list.length - 1;
  for (let i = len; i >= 0; --i) {
    newArray.push(list[i]);
  }
  return newArray;
};
