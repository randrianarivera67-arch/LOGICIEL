import re

p = open('pay.js', encoding='utf-8').read()

# 1. Averina ny lg_cart fotsiny (localStorage = tsirairay navigateur)
p = re.sub(
    r"var CART_KEY='lg_cart_'[^;]+;var CART=pget\(CART_KEY,\[\]\);",
    "var CART=pget('lg_cart',[]);",
    p
)

# 2. Averina ny pset('lg_cart',CART)
p = p.replace("pset(CART_KEY,CART)", "pset('lg_cart',CART)")

# 3. Fafao ny SETTINGS session-based (tsy nisy taloha)
p = p.replace("pset('lg_settings_'+CART_KEY,SETTINGS)", "pset('lg_settings',SETTINGS)")

open('pay.js', 'w', encoding='utf-8').write(p)
print('OK pay.js v38 - revert cart to localStorage (tsirairay navigateur)')
