base = 'https://cshmobqykkqjmusnkeom.supabase.co/functions/v1/tg?p='
try:
    urls = dict(l.strip().split('=', 1) for l in open('tg_urls.txt') if '=' in l)
except Exception:
    urls = {}
files = ['pay.js', 'index.html', 'hero.css', 'pay.css', 'app1.js', 'app2.js', 'hero.js']
for f in files:
    try:
        c = open(f, encoding='utf-8').read()
    except Exception:
        continue
    o = c
    for name, p in urls.items():
        if p:
            c = c.replace(base + p, 'img/' + name + '.png')
    # raha banga ny path: esory ny proxy URL foana (base fotsiny)
    c = c.replace(base + "'", "'").replace(base + '"', '"')
    if c != o:
        open(f, 'w', encoding='utf-8').write(c)
        print('OK ' + f)
print('Logo -> img/ (GitHub)')
