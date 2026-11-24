// Entry program for the "Post the Meme, Win the Feed" bounty (Node 22, stdlib only).
// The house gate reads POST.json from /output, so this program copies it there.
// It also copies the meme itself, so the run's output holds the entry's picture.
// Run locally with: mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { join as joinPath } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(outDir, { recursive: true });

const postFile = joinPath(botDir, 'POST.json');
if (!existsSync(postFile)) {
  console.error(`POST.json not found in ${botDir}`);
  process.exit(1);
}
copyFileSync(postFile, joinPath(outDir, 'POST.json'));

const memeFile = joinPath(botDir, 'meme.png');
if (existsSync(memeFile)) {
  copyFileSync(memeFile, joinPath(outDir, 'meme.png'));
}

console.log(`POST.json copied to ${outDir}`);
