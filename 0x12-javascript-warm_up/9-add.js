#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

function add (a, b) {
  return (Number(a) + Number(b));
}

if (process.argv.length < 4) {
  console.log('NaN');
} else {
  if (arg1 === undefined || isNaN(arg1) || arg2 === undefined || isNaN(arg2)) {
    console.log('NaN');
  } else {
    console.log(add(arg1, arg2));
  }
}
