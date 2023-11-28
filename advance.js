const prompt = require('prompt-sync')();

function canEmptyPiles(A, B) {
  // Cari GCD dari A dan B
  while (B !== 0) {
      const temp = B;
      B = A % B;
      A = temp;
  }
  const gcd = A;

  // Jika jumlah koin di kedua tumpukan adalah ganjil dan positif, atau salah satu tumpukan memiliki satu koin, maka kita dapat mengosongkan tumpukan
  if (((A + B) % 3 === 0 && Math.abs(2 * A - B) % 3 === 0 && Math.abs(2 * B - A) % 3 === 0 && (A + B) > 0) || A === 1 || B === 1) {
      return "YES";
  }
  // Jika tidak, kita tidak dapat mengosongkan tumpukan
  else {
      return "NO";
  }
}

// Input
const T = parseInt(prompt("Masukkan jumlah input: "));

// Proses input
for (let i = 0; i < T; i++) {
  const [A, B] = prompt("Masukkan jumlah koin tumpukan kiri dan kanan: ").split(" ").map(Number);
  const result = canEmptyPiles(A, B);
  console.log(result);
}
