import re
c = open('index.html', encoding='utf-8').read()

# 1. Esorina ny stats amin'ny accueil
stats = '''<div class="stats">
<div><b id="statCount">0</b><span>Produits disponibles</span></div>
<div><b id="statLog">0</b><span>Logiciels</span></div>
<div><b id="statApp">0</b><span>Applications</span></div>
</div>'''
c = c.replace(stats, '')

# 2. Alefa eo ambony ny kicker ny barre de recherche
m = re.search(r'<div class="search">.*?</div>', c, flags=re.S)
if m:
    s = m.group(0)
    c = c.replace(s, '', 1)
    c = c.replace('<p class="stage-kicker">', s + '\n<p class="stage-kicker">', 1)

open('index.html', 'w', encoding='utf-8').write(c)

# 3. Guard renderStats ao amin'ny app1.js (mba tsy error raha tsy misy stats)
a = open('app1.js', encoding='utf-8').read()
old_rs = "function renderStats(){gid('statCount').textContent=state.list.length;gid('statLog').textContent=state.list.filter(function(i){return(i.type||'Logiciel')==='Logiciel'}).length;gid('statApp').textContent=state.list.filter(function(i){return i.type==='Application'}).length}"
new_rs = "function renderStats(){var a=gid('statCount'),b=gid('statLog'),d=gid('statApp');if(a)a.textContent=state.list.length;if(b)b.textContent=state.list.filter(function(i){return(i.type||'Logiciel')==='Logiciel'}).length;if(d)d.textContent=state.list.filter(function(i){return i.type==='Application'}).length}"
if old_rs in a:
    a = a.replace(old_rs, new_rs)
    open('app1.js', 'w', encoding='utf-8').write(a)
    print('OK - stats esorina + recherche ambony + renderStats guarded')
else:
    print('OK - html vita (renderStats efa guarded na hafa)')

# 4. CSS kely
css = open('hero.css', encoding='utf-8').read()
if '.hero .search{margin-bottom' not in css:
    css += '\n.hero .search{margin-bottom:14px}\n'
    open('hero.css', 'w', encoding='utf-8').write(css)
