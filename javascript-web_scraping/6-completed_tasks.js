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
  const todos = JSON.parse(body.toString());
  const countId = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

  for (const item of todos) {
    if (item.userId && item.completed) {
      countId[item.userId - 1] += 1;
    }
  }
  const result = {};
  for (let i = 1; i <= 10; i++) {
    result[`${i}`] = countId[i - 1];
  }
  console.log(result);
});
