# Star Wars Characters

This script is designed to retrieve and display all characters from a specific Star Wars movie using the Star Wars API. It takes a Movie ID as a positional argument and then fetches the character data associated with that movie from the API's `/films/` endpoint. The script utilizes the `request` module to make API calls and then prints out the character names in the same order as the `characters` list in the `/films/` endpoint.

## Usage

To use this script, follow these steps:

1. Clone the GitHub repository `alx-interview`.
2. Navigate to the `0x06-starwars_api` directory.
3. Make sure you have Node.js and the `request` module installed.
4. Run the script by executing the following command in your terminal:

   ```
   ./0-starwars_characters.js <Movie_ID>
   ```

   Replace `<Movie_ID>` with the ID of the desired Star Wars movie. For example, if you want to retrieve characters from "Return of the Jedi," you would use the Movie ID `3`.

5. The script will then fetch the character data from the API and display the character names, one per line, in the same order as the `characters` list in the `/films/` endpoint.

## Example

Here's an example of how to use the script:

```
node 0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## Dependencies

This script relies on the following components:

- Node.js: Make sure you have Node.js installed on your system.
- `request` module: You can install it using the following command:

  ```
  npm install request
  ```
