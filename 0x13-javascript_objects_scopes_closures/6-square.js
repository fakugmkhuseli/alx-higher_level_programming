#!/usr/bin/node
const SquareP = require('./5-square.js');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++)
    }
    console.log(c.repeat(this.width));
  }
}

module.exports = Square;
