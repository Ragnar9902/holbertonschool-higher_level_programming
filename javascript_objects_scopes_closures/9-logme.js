#!/usr/bin/node
const listI = [];
exports.logMe = function (item) {
  if (item) {
    console.log(listI.length + ': ' + item);
    listI.push(item);
  }
};
