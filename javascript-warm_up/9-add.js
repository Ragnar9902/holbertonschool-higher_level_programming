#!/usr/bin/node
const process = require('process');
if (parseInt(process.argv[2]) && parseInt(process.argv[3])) {
  const numA = parseInt(process.argv[2]);
  const numB = parseInt(process.argv[3]);

  console.log(numA + numB);
} else {
  console.log(parseInt(process.argv[2]));
}
