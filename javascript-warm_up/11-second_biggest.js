#!/usr/bin/node
const process = require('process');
const argv = process.argv.slice(2, process.argv.length);
function seconbiger (list) {
  if (list.length <= 1) {
    return 0;
  }

  return list.sort(function (a, b) { return a - b; }).reverse()[1];
}
if (parseInt(process.argv[2])) {
  const lisNum = [];
  for (let i = 0; i < argv.length; i++) {
    lisNum.push(parseInt(argv[i]));
  }
  console.log(seconbiger(lisNum));
} else {
  console.log(0);
}
