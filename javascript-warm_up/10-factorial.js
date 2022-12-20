#!/usr/bin/node
const process = require('process');

function factorial (n) {
  if (n === 1) {
    return 1;
  }
  if (n > 89) {
    return 'Infinity';
  }
  return n * factorial(n - 1);
}
if (parseInt(process.argv[2])) {
  const num = parseInt(process.argv[2]);

  console.log(factorial(num));
} else {
  console.log(1);
}
