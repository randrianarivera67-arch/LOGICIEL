import re

p = open('pay.js', encoding='utf-8').read()

# 1. Soloina ny lg_cart amin'ny session-based key
p = p.replace("var CART=pget('lg_cart',[]);", "var CART_KEY='lg_cart_'+(sessionStorage.getItem('lg_session')||(function(){var s='s'+Date.now().toString(36);sessionStorage.setItem('lg_session',s);return s})());var CART=pget(CART_KEY,[]);")

# 2. Soloina ny pset('lg_cart',...) amin'ny session-based
p = p.replace("pset('lg_cart',CART)", "pset(CART_KEY,CART)")

# 3. Soloina ny pset('lg_settings',...) amin'ny session-based (raha misy)
p = p.replace("pset('lg_settings',SETTINGS)", "pset('lg_settings_'+CART_KEY,SETTINGS)")

open('pay.js', 'w', encoding='utf-8').write(p)
print('OK pay.js v37 - cart tsirairay session')
