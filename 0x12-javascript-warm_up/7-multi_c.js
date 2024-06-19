#!/usr/bin/node

const arg = process.argv[2];
let num = parseInt(arg);

if (process.argv.length <= 2) {
  console.log('Missing number of occurrences');
} else {
  if (!isNaN(num) && num > 1) {
    while (num !== 0) {
      console.log('C is fun');
      num--;
    }
  }
}
