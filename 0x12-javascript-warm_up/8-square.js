#!/usr/bin/node

const arg = process.argv[2];
let num = parseInt(arg);

if (process.argv.length <= 2 || isNaN(num)) {
  console.log('Missing size');
} else {
  if (!isNaN(num) && num > 1) {
    let i = num;
    while (num !== 0) {
      console.log('x'.repeat(i));
      num--;
    }
  }
}
