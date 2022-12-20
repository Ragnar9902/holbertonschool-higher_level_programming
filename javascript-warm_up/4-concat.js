#!/usr/bin/node
const process = require('process');

const myargs = process.argv;

if (myargs.length === 2) {
  console.log('undefined is undefined');
}
if (myargs.length === 3) {
  console.log(myargs[2] + ' is undefined');
}
if (myargs.length >= 4) {
  console.log(myargs[2] + ' is ' + myargs[3]);
}
