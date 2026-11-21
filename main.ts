// GTA 6 clip entry (Node 22, standard library only).
// Copies VIDEO.json (the YouTube video's address) from the repository to /output.
// The video itself is the entry: the house reads it through the YouTube Data API.
import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = fileURLToPath(new URL('.', import.meta.url));
const out = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const video = join(here, 'VIDEO.json');
if (!existsSync(video)) {
  process.stderr.write('gta6 clip: no VIDEO.json at the repository root: post the clip on YouTube first, then write its URL into VIDEO.json\n');
  process.exit(2);
}
mkdirSync(out, { recursive: true });
copyFileSync(video, join(out, 'VIDEO.json'));
process.stdout.write(`gta6 clip: copied VIDEO.json to ${join(out, 'VIDEO.json')}\n`);
