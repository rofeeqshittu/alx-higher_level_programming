#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (process.argv.length < 4) {
  console.log('NaN');
} else {
  if (arg1 === undefined || isNaN(arg1) || arg2 === undefined || isNaN(arg2)) {
    console.log('NaN');
  } else {
    console.log(Number(arg1) + Number(arg2));
  }
}
