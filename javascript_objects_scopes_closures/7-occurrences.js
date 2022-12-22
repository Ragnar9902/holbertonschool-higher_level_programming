#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccu = 0;
  for (const elem of list) {
    if (elem === searchElement) {
      nOccu += 1;
    }
  }
  return nOccu;
};
