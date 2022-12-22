#!/usr/bin/node
const fs = require('fs');
const process = require('process');

if (process.argv[2]) {
  fs.readFile(process.argv[2], { encoding: 'utf-8' }, (err, data) => {
    if (err) {
      console.log(err);
    }
    console.log(data);
  });
}
