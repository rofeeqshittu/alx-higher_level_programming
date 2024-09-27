#!/usr/bin/node
// Import the 'request' module
const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Construct the API URL
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the API
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    if (movieData.title) {
      // Print the title of the movie
      console.log(movieData.title);
    } else {
      console.log('Movie not found');
    }
  }
});
