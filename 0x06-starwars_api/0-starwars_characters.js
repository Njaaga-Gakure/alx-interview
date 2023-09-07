#!/usr/bin/node

const request = require('request');
const args = process.argv;

if (args.length !== 3) {
  console.log('usage: 0-starwars_characters movieID');
} else {
  request(`https://swapi-api.alx-tools.com/api/films/${args[2]}`, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const { characters } = JSON.parse(body);
      const fetchInOrder = (characters, index) => {
        if (index >= characters.length) {
          return;
        }
        const characterUrl = characters[index];
        request(characterUrl, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            const { name } = JSON.parse(body);
            console.log(name);
            fetchInOrder(characters, index + 1);
          }
        });
      };
      fetchInOrder(characters, 0);
    }
  });
}
