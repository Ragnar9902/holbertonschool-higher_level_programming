#!/usr/bin/node
const process = require('process');
if (parseInt(process.argv[2]) && parseInt(process.argv[3])) {
  const num_a = parseInt(process.argv[2]);
  const num_b = parseInt(process.argv[3]);

  console.log(num_a + num_b);
} else {
  console.log(parseInt(process.argv[2]));
}
