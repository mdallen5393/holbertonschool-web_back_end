// Program that displays a string, takes inputs, and
// responds

const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('Welcome to Holberton School, what is your name?\n', name => {
  if (name.trim() === '') {
    process.stdout.write('No name provided. Exiting...\n');
    process.exit(0);
  }
  process.stdout.write(`Your name is: ${name}\r`);
  readline.close();
});

readline.on('close', () => {
  process.stdout.write('This important software is now closing\n');
})