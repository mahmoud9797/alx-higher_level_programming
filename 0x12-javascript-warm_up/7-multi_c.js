#!/usr/bin/node
const word = 'C is fun';
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const n = parseInt(process.argv[2]);
  for (let i = 0; i < n; i++) {
    console.log(word);
  }
}
