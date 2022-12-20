#!/usr/bin/node
const process = require('process');

const myargs = process.argv;

if (myargs[2]) {
  console.log(myargs[2]);
} else {
  console.log('No argument');
}
