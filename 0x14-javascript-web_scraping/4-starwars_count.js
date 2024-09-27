#!/usr/bin/node
// Import the 'request' module
const request = require('request');

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movies = JSON.parse(body).results; // Parse the response to get the movies
    let count = 0; // Initialize the counter for Wedge Antilles

    // Loop through each movie to check for the character
    movies.forEach(movie => {
      if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++; // Increment the counter if Wedge Antilles is found
      }
    });

    // Print the total count of movies
    console.log(count);
  }
});
