import json, urllib.request, urllib.parse

URL = 'https://cshmobqykkqjmusnkeom.supabase.co'
KEY = 'sb_publishable_rveJ3wjRsYkcPWYdaPSqJA_RKSiGqDF'

print('🔍 Maka ny produits...')
req = urllib.request.Request(URL + '/rest/v1/products?select=id,name,image',
                             headers={'apikey': KEY})
rows = json.load(urllib.request.urlopen(req))
print(f'✅ {len(rows)} produits hita\n')

def clean(img):
    if not img: return img
    if '/file/bot' in img: return img.split('/file/bot', 1)[1].split('/', 1)[1]
    if '?p=' in img: return urllib.parse.unquote(img.split('?p=', 1)[1])
    if img.startswith('http'): return ''
    return img

fixed = 0
for r in rows:
    old = r['image'] or ''
    c = clean(old)
    if c != old:
        try:
            rq = urllib.request.Request(URL + '/rest/v1/products?id=eq.' + r['id'],
                data=json.dumps({'image': c}).encode(),
                headers={'apikey': KEY, 'Content-Type': 'application/json',
                         'x-admin-key': 'LOGIPLUS2026', 'Prefer': 'return=minimal'},
                method='PATCH')
            urllib.request.urlopen(rq)
            print(f'✅ FIX {r["id"]} ({r["name"]}) -> {c[:60]}')
            fixed += 1
        except Exception as e:
            print(f'❌ ERR {r["id"]}: {e}')
    else:
        print(f'OK  {r["id"]} ({r["name"]})')

print(f'\n📊 Vita: {fixed}/{len(rows)} produits voafafa')
