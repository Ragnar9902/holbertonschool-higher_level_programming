#!/usr/bin/node
const request = require('request');
const process = require('process');
const fs = require('fs');
const argv = process.argv;
const url = argv[2];
const filename = argv[3];

request(url, (error, response, body) => {
  if (!error || response.statusCode === 200) {
    const data = JSON.stringify(body);
    fs.writeFile(filename, JSON.parse(data), 'utf-8', err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
