import json, urllib.request, os

URL = 'https://cshmobqykkqjmusnkeom.supabase.co'
KEY = 'sb_publishable_rveJ3wjRsYkcPWYdaPSqJA_RKSiGqDF'

# 1. Maka ny produits rehetra
req = urllib.request.Request(URL + '/rest/v1/products?select=id,name,image', headers={'apikey': KEY})
rows = json.load(urllib.request.urlopen(req))

print(f'📋 {len(rows)} produits — mila alefa indray ny sary\n')

# 2. Jereo raha misy sary ao amin'ny img/
if os.path.exists('img'):
    images = [f for f in os.listdir('img') if f.endswith(('.png','.jpg','.jpeg'))]
    print(f'✅ {len(images)} sary hita ao amin\'ny img/')
    for img in images[:5]:
        print(f'   - {img}')
else:
    print('❌ Tsy misy sary ao amin\'ny img/')
    print('💡 Alefaso ny sary taloha ao amin\'ny dossier img/ aloha')
    raise SystemExit

# 3. Map products -> images (ohatra fotsiny)
print('\n🔧 Fomba:')
print('1. Manokatra admin → Modifier → "Choisir" → misafidy sary → Publier')
print('2. Na: mamorona mapping manuel (produit -> sary)')
print('3. Na: alefa indray ny sary rehetra amin\'ny script')
