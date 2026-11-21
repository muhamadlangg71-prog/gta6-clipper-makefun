# Cut a vertical YouTube Short from GTA 6 Trailer 2 + make.fun pitch (ffmpeg).
# Segment: 140s-160s (2:20-2:40) — airboat chase -> Vice City sunset skyline.
# Pitch (last 3s, on screen): "My AI agent made this clip. Earn on make.fun" + ghost badge.
# NIM timed out twice (read timeout) — segment + pitch chosen by agent from the
# trailer contact sheet; NIM's earlier meme consult already set the make.fun voice.
import subprocess, os, sys

BASE = '/home/hatch/workspace/makefun/gta6-clipper-01'
SRC = f'{BASE}/footage/gta6-trailer2.mp4'
GHOST = '/home/hatch/workspace/makefun/gta6-meme-x-01/assets/icon-512.png'
OUT = f'{BASE}/work/clip.mp4'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

START, DUR = 140, 20          # 2:20-2:40
PITCH_START = 17              # pitch appears in the last 3s (17-20s)
PITCH_TEXT = 'My AI agent made this clip.'
PITCH_TEXT2 = 'Earn on make.fun'

# Build a circular ghost badge (same as the meme) for the overlay
from PIL import Image, ImageDraw
icon = Image.open(GHOST).convert('RGBA')
mask = Image.new('L', icon.size, 0)
md = ImageDraw.Draw(mask)
md.ellipse([18, 18, 494, 494], fill=255)
badge = Image.new('RGBA', icon.size, (0, 0, 0, 0))
badge.paste(icon, (0, 0), mask)
badge = badge.resize((180, 180), Image.LANCZOS)
badge_path = f'{BASE}/footage/ghost-badge.png'
badge.save(badge_path)
print('ghost badge saved:', badge_path)

# ffmpeg: trim, center-crop to 9:16, scale to 720x1280, overlay pitch text + ghost (last 3s)
# drawtext with box for readability; escape the text for the filter
def esc(s):
    return s.replace("'", "\\'").replace(':', '\\:')

vf = (
    f"trim=start={START}:duration={DUR},setpts=PTS-STARTPTS,"
    f"crop=405:720:(in_w-405)/2:(in_h-720)/2,scale=720:1280,"
    f"drawtext=fontfile={FONT}:text='{esc(PITCH_TEXT)}':fontsize=44:fontcolor=white:borderw=3:bordercolor=black:"
    f"x=(w-text_w)/2:y=880:enable='gte(t\\,{PITCH_START})',"
    f"drawtext=fontfile={FONT}:text='{esc(PITCH_TEXT2)}':fontsize=52:fontcolor=yellow:borderw=3:bordercolor=black:"
    f"x=(w-text_w)/2:y=950:enable='gte(t\\,{PITCH_START})'"
)
cmd = [
    'ffmpeg', '-y', '-v', 'error',
    '-i', SRC,
    '-i', badge_path,
    '-filter_complex',
    f"[0:v]{vf}[v];[1:v]scale=180:180[bg];[v][bg]overlay=(W-180)/2:620:enable='gte(t\\,{PITCH_START})'[out]",
    '-map', '[out]', '-map', '0:a',
    '-t', str(DUR),
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '20',
    '-c:a', 'aac', '-b:a', '128k',
    '-movflags', '+faststart',
    OUT,
]
print('running ffmpeg...')
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0:
    print('ffmpeg FAILED:', r.stderr[-2000:])
    sys.exit(1)
print('clip written:', OUT, os.path.getsize(OUT), 'bytes')
# probe
p = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration,size','-show_entries','stream=width,height,codec_name','-of','default=noprint_wrappers=1', OUT], capture_output=True, text=True)
print(p.stdout)
