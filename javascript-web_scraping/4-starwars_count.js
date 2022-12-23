#!/usr/bin/node
const request = require('request');
const process = require('process');
const argv = process.argv;
const url = argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    console.log(response);
  }
  const results = JSON.parse(body.toString()).results;
  let nOcc = 0;
  for (const film of results) {
    for (const chara of film.characters) {
      if (chara.includes('18')) {
        nOcc += 1;
      }
    }
  }
  console.log(nOcc);
});
