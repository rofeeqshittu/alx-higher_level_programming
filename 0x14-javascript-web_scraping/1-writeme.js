#!/usr/bin/node
// Import the 'fs' module to interact with the file system
const fs = require('fs');

// Get the file path and the string to write from the command-line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file with utf-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    // Print the error object if an error occurs
    console.error(err);
  }
});
