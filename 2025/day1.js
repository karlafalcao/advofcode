function countPassesDuring(start, direction, dist) {
  // direction: +1 for R, -1 for L
  // find smallest k in 1..dist with (start + k*direction) % 100 == 0
  const s = start
  let k0;
  if (direction === 1) {
    k0 = (100 - s) % 100;
  } else {
    k0 = s % 100;
  }
  const firstK = k0 === 0 ? 100 : k0;
  if (firstK > dist) return 0;
  return 1 + Math.floor((dist - firstK) / 100);
}


let pos = 50;
let part1 = 0;
let part2 = 0;

for (const line of directions) {
  const dirChar = line[0];
  const d = parseInt(line.slice(1), 10);
  const dirVal = dirChar === 'R' ? 1 : -1;

  part2 += countPassesDuring(pos, dirVal, d);

  pos = ((pos + dirVal * d) % 100 + 100) % 100;

  if (pos === 0) part1 += 1;
}

console.log(part1);
console.log(part2);