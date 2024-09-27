#!/usr/bin/node
// Import the 'request' module
const request = require('request');

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error if one occurs
  } else {
    // Parse the response body as JSON
    const tasks = JSON.parse(body);
    
    // Create an object to store the count of completed tasks by user ID
    const completedTasksCount = {};
    
    // Iterate through the tasks and count completed tasks for each user ID
    tasks.forEach(task => {
      if (task.completed) {
        if (!completedTasksCount[task.userId]) {
          completedTasksCount[task.userId] = 0;
        }
        completedTasksCount[task.userId]++;
      }
    });

    // Print the result
    console.log(completedTasksCount);
  }
});
