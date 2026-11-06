import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
index = json.loads((root/'data/groups/index.json').read_text(encoding='utf-8'))
errors = []
for entry in index:
    data = json.loads((root/entry['file']).read_text(encoding='utf-8'))
    song_ids = {s['id'] for s in data['songs']}
    album_ids = {a['id'] for a in data['albums']}
    for song in data['songs']:
        if song['albumId'] not in album_ids: errors.append(f"{song['id']}: missing album {song['albumId']}")
        if not song.get('officialSource','').startswith('https://'): errors.append(f"{song['id']}: missing official source")
    for album in data['albums']:
        for sid in album['songIds']:
            if sid not in song_ids: errors.append(f"{album['id']}: missing song {sid}")
if errors:
    print('Validation failed:'); print('\n'.join(errors)); raise SystemExit(1)
print('JSON structure and internal references look valid.')
