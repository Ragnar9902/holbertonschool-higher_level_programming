#!/usr/bin/node
const request = require('request');
const process = require('process');
const fs = require('fs');
const argv = process.argv;
const url = argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    console.log(response);
  }
  const content = body.toString();
  fs.writeFile(argv[3], content, function (err) {
    console.error(err);
  })
});