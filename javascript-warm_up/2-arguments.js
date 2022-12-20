#!/usr/bin/node
const process = require('process');

const myargs = process.argv;

if (myargs.length === 2) {
  console.log('No argument');
}
if (myargs.length === 3) {
  console.log('Argument found');
}
if (myargs.length >= 4) {
  console.log('Arguments found');
}
