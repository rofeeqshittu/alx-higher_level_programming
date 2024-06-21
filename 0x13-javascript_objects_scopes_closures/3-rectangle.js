#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      // Create an empty object by not initializing any properties
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('x'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
