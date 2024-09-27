#!/usr/bin/node
const request = require('request');

// Make a GET request to the URL provided as the first command-line argument
request.get(process.argv[2], (error, response) => {
  if (error) {
    console.error(error);
  } else {
    // Print the status code
    console.log(`code: ${response.statusCode}`);
  }
});
