"""Build picks.js from the reviewed pass list. Usage: python3 tools/build-picks.py pass.txt [more.txt ...] > picks.js"""
import sys, json
bar = open(sys.argv[1].rsplit('/', 1)[0] + '/bar.md').read().strip() if '/' in sys.argv[1] else ''
rows, seen = [], set()
for f in sys.argv[1:]:
    for line in open(f, encoding='utf-8'):
        parts = [x.strip() for x in line.split('|')]
        if len(parts) < 2 or not parts[0] or parts[0] in seen: continue
        seen.add(parts[0])
        tags = parts[2] if len(parts) > 2 else ''
        fx, fy = 50, 50
        if len(parts) > 3 and ',' in parts[3]:
            try: fx, fy = [int(round(float(v))) for v in parts[3].split(',')[:2]]
            except ValueError: pass
        rows.append([parts[0], parts[1], tags, fx, fy])
print('/* Hand-picked art for the wall. Only images that passed a separate review against this bar are listed.')
for l in bar.splitlines(): print('   ' + l.replace('*/', '* /'))
print('   Entry: [Commons file title, category, tags, crop focus x %, crop focus y %]. */')
print('var PICKS = [')
print(',\n'.join('  ' + json.dumps(r, ensure_ascii=False) for r in rows))
print('];')
