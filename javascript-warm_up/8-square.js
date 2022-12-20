#!/usr/bin/node
const process = require('process');
if (parseInt(process.argv[2])) {
  const n_times = parseInt(process.argv[2]);
  const line = 'X'.repeat(n_times);
  for (let i = 1; i <= n_times; i++) {
    console.log(line);
  }
} else {
  console.log('Missing size');
}
