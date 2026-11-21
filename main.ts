// GTA 6 clip entry (Node 22, standard library only).
// Copies VIDEO.json (the YouTube video's address) from the repository to /output.
// The video itself is the entry: the house reads it through the YouTube Data API.
// The video is a public vertical Short (720x1280, 20s) cut from Rockstar's
// GTA 6 Trailer 2; its last 3 seconds pitch make.fun on screen, and its
// description carries the bounty line and the entry's play code.
import { copyFileSync, existsSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = fileURLToPath(new URL('.', import.meta.url));
const out = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const video = join(here, 'VIDEO.json');
if (!existsSync(video)) {
  process.stderr.write('gta6 clip: no VIDEO.json at the repository root: post the clip on YouTube first, then write its URL into VIDEO.json\n');
  process.exit(2);
}
const { url } = JSON.parse(readFileSync(video, 'utf8'));
if (typeof url !== 'string' || !/^https:\/\/(www\.)?(youtube\.com\/shorts\/|youtu\.be\/)/.test(url)) {
  process.stderr.write(`gta6 clip: VIDEO.json must name a public YouTube Short URL, got: ${url}\n`);
  process.exit(2);
}
mkdirSync(out, { recursive: true });
copyFileSync(video, join(out, 'VIDEO.json'));
process.stdout.write(`gta6 clip: copied VIDEO.json to ${join(out, 'VIDEO.json')}\n`);
