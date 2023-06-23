// Program that displays a string, takes inputs, and
// responds

const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('Welcome to Holberton School, what is your name?\n', name => {
  console.log(`Your name is: ${name}!`);
  readline.close();
});

if (!process.stdin.isTTY) {
  process.on('exit', function(code) {
    console.log("This important software is now closing");
  });
}