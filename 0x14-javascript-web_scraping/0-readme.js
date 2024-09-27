#!/usr/bin/node
// Import the 'fs' module to interact with the file system
const fs = require('fs');

// Get the file path from the command-line arguments
const filePath = process.argv[2];

// Read the file with utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Print the error object if an error occurs
    console.error(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
