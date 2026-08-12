import re
c = open('index.html', encoding='utf-8').read()
c = re.sub(r'<meta name="viewport"[^>]*>', '<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">', c, count=1)
open('index.html', 'w', encoding='utf-8').write(c)
css = open('hero.css', encoding='utf-8').read()
add = '''
.nav{position:fixed!important;top:0;left:0;right:0;z-index:100}
body{padding-top:74px}
.theme-fab,.pm-fab{position:fixed!important;z-index:70}
html{touch-action:manipulation}
'''
if '.nav{position:fixed' not in css:
    css += add
    open('hero.css', 'w', encoding='utf-8').write(css)
print('OK v9 - topbar flottant + tsy misy zoom')
