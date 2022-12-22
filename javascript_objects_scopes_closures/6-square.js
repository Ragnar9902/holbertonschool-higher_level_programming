#!/usr/bin/node

const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c) {
      const line = c.repeat(this.width);
      for (let i = 1; i <= this.height; i++) {
        console.log(line);
      }
    }
  }
};
