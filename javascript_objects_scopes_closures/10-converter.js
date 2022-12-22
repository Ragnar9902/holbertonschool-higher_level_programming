#!/usr/bin/node
exports.converter = function (base) {
  function convert (number) {
    number.toString(base);
  }
  return convert;
};
