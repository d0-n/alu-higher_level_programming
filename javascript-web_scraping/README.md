# JavaScript - Web scraping

This project uses Node.js to read files, write files, and request data from APIs.

The scripts use the `fs` module for files and the `request` module for web requests.

## Files

- `0-readme.js` - reads a file and prints its content.
- `1-writeme.js` - writes text into a file.
- `2-statuscode.js` - prints the status code of a GET request.
- `3-starwars_title.js` - prints a Star Wars movie title using the movie id.
- `4-starwars_count.js` - counts movies with Wedge Antilles.
- `5-request_store.js` - gets a webpage and stores it in a file.
- `6-completed_tasks.js` - counts completed tasks by user id.

## Requirements

- Node.js
- `request` module
- semistandard style

## Usage

```bash
./0-readme.js file_name
./1-writeme.js file_name "text"
./2-statuscode.js url
./3-starwars_title.js movie_id
./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
./5-request_store.js url file_name
./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
```
