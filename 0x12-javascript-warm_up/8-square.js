#!/usr/bin/node

const arg = process.argv[2];
let num = parseInt(arg);

if (isNaN(num) || num <= 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('x'.repeat(num));
  }
}
