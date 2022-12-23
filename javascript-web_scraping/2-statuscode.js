#!/usr/bin/node
const request = require('request');
const process = require('process');
const argv = process.argv;

request(argv[2], (err, response, body) => {
    if (err) {
        console.error(err);
    }
    console.log('code: ' + response.statusCode);
});