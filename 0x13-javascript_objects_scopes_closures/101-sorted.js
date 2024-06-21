#!/usr/bin/node
const { dict } = require('./101-data'); // Importing the dict dictionary from 101-data.js

// Initialize an empty object to store the new dictionary
const occurrencesById = {};

// Iterate through the keys (user ids) and values (occurrences) of the original dict
Object.keys(dict).forEach(userId => {
  const occurrences = dict[userId];

  // If the occurrences is not yet a key in occurrencesById, initialize it as an empty array
  if (!occurrencesById[occurrences]) {
    occurrencesById[occurrences] = [];
  }

  // Push the userId into the array corresponding to its occurrences
  occurrencesById[occurrences].push(userId);
});

// Print the new dictionary occurrencesById
console.log(occurrencesById);
