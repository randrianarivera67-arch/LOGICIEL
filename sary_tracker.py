import json, urllib.request
URL = 'https://cshmobqykkqjmusnkeom.supabase.co'
KEY = 'sb_publishable_rveJ3wjRsYkcPWYdaPSqJA_RKSiGqDF'
req = urllib.request.Request(URL + '/rest/v1/products?select=id,name,image', headers={'apikey': KEY})
rows = json.load(urllib.request.urlopen(req))
print('📋 LISTA PRODUITS — mila alefa ny sary:\n')
for i, r in enumerate(rows, 1):
    print(f'{i:2}. {r["name"]:<30} (ID: {r["id"]})')
print(f'\n🎯 FOMBA (ho an\'ny tsirairay):')
print('1. Open: logiplus.pages.dev/admin.html')
print('2. Login (admin123) → Produits → Modifier')
print('3. Ao amin\'ny "Image" → tsindrio "Choisir" → misafidy sary')
print('4. Miandry ⏳ Upload → Publier')
print('5. Averino ho an\'ny 16 produits (~30 min)')
