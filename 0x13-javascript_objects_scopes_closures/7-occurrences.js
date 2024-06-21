#!/usr/env/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      nOccurrences = nOccurrences + 1;
    }
  }
  return nOccurrences;
};
