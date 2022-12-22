#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      return this;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    const line = 'X'.repeat(this.width);
    for (let i = 1; i <= this.height; i++) {
      console.log(line);
    }
  }
};
