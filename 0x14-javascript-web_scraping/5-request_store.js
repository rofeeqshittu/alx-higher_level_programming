#!/usr/bin/node
// Import the 'request' module
const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error if one occurs
  } else {
    // Write the body response to the specified file in UTF-8 encoding
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error(err); // Print the error if writing fails
      }
    });
  }
});
