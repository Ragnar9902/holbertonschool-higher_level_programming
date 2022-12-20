#!/usr/bin/node
const process = require('process');
if (parseInt(process.argv[2])) {
  const line = 'C is fun';
  const ntimes = parseInt(process.argv[2]);
  for (let i = 1; i <= ntimes; i++) {
    console.log(line);
  }
} else {
  console.log('Missing number of occurrences');
}
