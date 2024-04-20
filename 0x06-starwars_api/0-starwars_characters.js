#!/usr/bin/node
// Import the necessary modules
const request = require('request');

function requestSync (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve({ response, body });
      }
    });
  });
}

async function fetchMovieData (movieId) {
  try {
    const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

    const { response, body } = await requestSync(movieUrl);

    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;

      for (const url of characters) {
        const { response: charResponse, body: charBody } = await requestSync(url);
        if (charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      }
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

const movieId = process.argv[2];

fetchMovieData(movieId);
