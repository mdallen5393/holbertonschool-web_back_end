// Program that displays a string, takes inputs, and
// responds

const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('Welcome to Holberton School, what is your name?\n', name => {
  process.stdout.write(`Your name is: ${name}\r`);
  readline.close();
});

process.on('close', function(code) {
  process.stdout.write("This important software is now closing\n");
});
