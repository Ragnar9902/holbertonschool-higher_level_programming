#!/usr/bin/node
const process = require('process');
const argv = process.argv.slice(2, process.argv.length);
function second_biger (list) {
  if (list.length <= 1) {
    return 0;
  }

  return list.sort(function (a, b) { return a - b; }).reverse()[1];
}
if (parseInt(process.argv[2])) {
  const list_num = [];
  for (let i = 0; i < argv.length; i++) {
    list_num.push(parseInt(argv[i]));
  }
  console.log(second_biger(list_num));
} else {
  console.log(0);
}
