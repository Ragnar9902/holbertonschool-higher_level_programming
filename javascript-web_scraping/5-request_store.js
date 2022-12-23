#!/usr/bin/node
const request = require('request');
const process = require('process');
const fs = require('fs');
const argv = process.argv;
const url = argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const content = JSON.parse(body.toString());
  fs.writeFile(argv[3], content, 'utf-8',function (err) {
    console.error(err);
  });
});
