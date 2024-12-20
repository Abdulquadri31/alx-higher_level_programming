#!/usr/bin/node
const Rectangle = require('./4-rectangle');

// Defines a class Square that extends Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Calls the constructor of Rectangle with width and height as size
  }
}

module.exports = Square;
