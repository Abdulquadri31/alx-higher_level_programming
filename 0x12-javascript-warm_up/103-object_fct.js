#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value += 1;  // Increment the value property
  }
};

console.log(myObject);
myObject.incr();  // Increment the value
console.log(myObject);
myObject.incr();  // Increment the value
console.log(myObject);
myObject.incr();  // Increment the value
console.log(myObject);
