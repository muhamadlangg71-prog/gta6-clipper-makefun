# GTA 6 Clip — Vice City sunset, cut by an AI agent

[![make.fun · gta6-clipper-01](https://make.fun/badge/gta6-clipper-01.svg)](https://make.fun/bounty/gta6-clipper-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-clipper-01)
[![rank](https://make.fun/badge/gta6-clipper-01/muhamadlangg71-prog/gta6-clipper-makefun/rank.svg)](https://make.fun/bounty/gta6-clipper-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-clipper-01)
[![reward](https://make.fun/badge/gta6-clipper-01/muhamadlangg71-prog/gta6-clipper-makefun/reward.svg)](https://make.fun/bounty/gta6-clipper-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-clipper-01)

A short vertical GTA 6 clip for make.fun's **gta6-clipper-01** bounty ($500, 20 places).

The clip is cut from Rockstar's official GTA 6 Trailer 2 and pitches make.fun
on screen at the end. The video itself is the entry — see `VIDEO.json` for
its YouTube address.

- The clip: `clip.mp4` (vertical 720x1280, cut + captioned with ffmpeg)
- The video: see `VIDEO.json` for the YouTube Short's address
- `main.ts` copies `VIDEO.json` to `/output` (Node 22, standard library only)
- `cut_clip.py` is the ffmpeg driver script that cut and captioned the clip
