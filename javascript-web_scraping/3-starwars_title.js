#!/usr/bin/node
const request = require('request');
const process = require('process');
const argv = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    console.log(response);
  }
  console.log(JSON.parse(body.toString()).title);
});
