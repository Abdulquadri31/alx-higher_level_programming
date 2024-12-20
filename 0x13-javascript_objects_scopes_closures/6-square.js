#!/usr/bin/node
const Square5 = require('./5-square');

// Defines a class Square that extends Square5
class Square extends Square5 {
  // Instance method to print the square using a specific character or 'X' by default
  charPrint (c) {
    const char = c || 'X'; // Use 'X' if c is undefined
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
