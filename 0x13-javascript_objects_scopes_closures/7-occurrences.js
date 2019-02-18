#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.filter(function (x) { return x === searchElement; }).length;
};
