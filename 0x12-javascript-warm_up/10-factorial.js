#!/usr/bin/node

function fact (num) {
  if (num === 1 || num === 0) {
    return 1;
  }

  return num * fact(num - 1);
}

const arg = parseInt(process.argv[2]);

if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(fact(arg));
}
