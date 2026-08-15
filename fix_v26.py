import re, subprocess, json
s = open('tg_upload.sh').read()
TOKEN = re.search(r'TOKEN="([^"]+)"', s).group(1)
CHAT = re.search(r'CHAT="([^"]+)"', s).group(1)
urls = {}
try:
    urls = dict(l.strip().split('=', 1) for l in open('tg_urls.txt') if '=' in l)
except Exception:
    pass
if not (urls.get('stage-bg') or '').strip():
    r = subprocess.run(['curl', '-s', '-F', 'chat_id=' + CHAT, '-F', 'document=@img/stage-bg.png',
        'https://api.telegram.org/bot' + TOKEN + '/sendDocument'], capture_output=True, text=True)
    try:
        p = json.loads(r.stdout)['result']['document']['file_path']
        urls['stage-bg'] = p
        open('tg_urls.txt', 'a').write('stage-bg=' + p + '\n')
        print('stage-bg ->', p)
    except Exception:
        print('stage-bg tsy voalefa:', r.stdout[:200])
base = 'https://cshmobqykkqjmusnkeom.supabase.co/functions/v1/tg?p='
for f in ['index.html', 'hero.css', 'pay.css', 'pay.js', 'app1.js', 'app2.js']:
    try:
        c = open(f, encoding='utf-8').read()
    except Exception:
        continue
    o = c
    for name, p in urls.items():
        if p:
            c = c.replace('img/' + name + '.png', base + p)
    if c != o:
        open(f, 'w', encoding='utf-8').write(c)
        print('OK ' + f)
