b = open('admin.js', encoding='utf-8').read()

# 1. CSS compact + horizontal scroll menu
i = b.find("st.textContent='")
j = b.find("';document.head.appendChild(st);")
newcss = '.adm-menu{display:flex;gap:6px;flex-wrap:nowrap;overflow-x:auto;margin:10px 0;padding-bottom:4px;scrollbar-width:none;-webkit-overflow-scrolling:touch}.adm-menu::-webkit-scrollbar{display:none}.adm-m{padding:7px 12px;flex:none;white-space:nowrap;border-radius:10px;border:1px solid var(--border);background:var(--ghost-bg);color:var(--muted);font-weight:600;font-size:.78rem;cursor:pointer;transition:.2s}.adm-m.active{background:var(--grad);color:#fff;border-color:transparent}.dash-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(86px,1fr));gap:8px}.dash-c{padding:10px 6px;text-align:center;cursor:pointer}.dash-c:active{transform:scale(.96)}.dash-c b{display:block;font-family:Sora;font-size:1.05rem;font-weight:800;background:var(--grad);-webkit-background-clip:text;color:transparent}.dash-c span{color:var(--muted);font-size:.66rem}#adminPanel .btn{padding:8px 13px;font-size:.78rem;border-radius:10px}#adminPanel .panel{padding:12px}'
b = b[:i] + "st.textContent='" + newcss + b[j:]

# 2. applyCatFilter : type filter koa
b = b.replace(
"function applyCatFilter(){var cat=window.__admCat||'Tous';var q=",
"function applyCatFilter(){var cat=window.__admCat||'Tous';var typ=window.__admType||'Tous';var q=")
b = b.replace(
"var items=(state.list||[]).filter(function(it){if(cat!=='Tous'&&(it.category||'Autre')!==cat)return false;",
"var items=(state.list||[]).filter(function(it){if(typ!=='Tous'&&(it.type||'Logiciel')!==typ)return false;if(cat!=='Tous'&&(it.category||'Autre')!==cat)return false;")

# 3. Dashboard cards : data-dash (clickable)
b = b.replace("<div class=\"panel dash-c\"><b>'+L.length+'</b><span>Produits</span></div>",
"<div class=\"panel dash-c\" data-dash=\"all\"><b>'+L.length+'</b><span>Produits</span></div>")
b = b.replace("<div class=\"panel dash-c\"><b>'+nbLog+'</b><span>Logiciels</span></div>",
"<div class=\"panel dash-c\" data-dash=\"log\"><b>'+nbLog+'</b><span>Logiciels</span></div>")
b = b.replace("<div class=\"panel dash-c\"><b>'+(L.length-nbLog)+'</b><span>Applications</span></div>",
"<div class=\"panel dash-c\" data-dash=\"app\"><b>'+(L.length-nbLog)+'</b><span>Applications</span></div>")
b = b.replace("<div class=\"panel dash-c\"><b>'+Object.keys(cats).length+'</b><span>Catégories</span></div>",
"<div class=\"panel dash-c\" data-dash=\"all\"><b>'+Object.keys(cats).length+'</b><span>Catégories</span></div>")
b = b.replace("<span>Téléchargements</span>", "<span>Téléch.</span>")

# 4. Top 5 : clickable -> edit
b = b.replace("return '<div style=\"display:flex;justify-content:space-between;gap:10px;",
"return '<div data-edit=\"'+esc(i.id)+'\" style=\"display:flex;justify-content:space-between;gap:10px;cursor:pointer;")

# 5. Répartition : clickable -> filter
b = b.replace("return '<div style=\"display:flex;justify-content:space-between;padding:8px 0;",
"return '<div data-cat=\"'+esc(c)+'\" style=\"display:flex;justify-content:space-between;padding:8px 0;cursor:pointer;")

# 6. Navigation : ao amin'ny admin ihany
s = b.find('function renderNav(){')
e = b.find("if(g('navLinks'))g('navLinks').innerHTML=h}")
if s > -1 and e > -1:
    e2 = e + len("if(g('navLinks'))g('navLinks').innerHTML=h}")
    newnav = '''function renderNav(){var cats=[],seen={};(state.list||[]).forEach(function(i){var c=i.category||'Autre';if(!seen[c]){seen[c]=1;cats.push(c)}});
var h="<p style='color:var(--muted);font-size:.8rem;margin-bottom:10px'>Navigation rapide (ao anatin'ny admin ihany):</p>";
for(var i=0;i<cats.length;i++){(function(c){h+='<button class="btn ghost" data-navcat="'+esc(c)+'">📂 '+esc(c)+'</button>'})(cats[i])}
h+='<button class="btn ghost" onclick="toggleTheme()">🌓 Clair / Sombre</button><button class="btn ghost" onclick="doLogout()">🚪 Déconnexion</button>';
if(g('navLinks'))g('navLinks').innerHTML=h}'''
    b = b[:s] + newnav + b[e2:]

# 7. navLinks : flex wrap
b = b.replace("style=\"display:flex;flex-direction:column;gap:8px\"></div></div>'",
"style=\"display:flex;gap:8px;flex-wrap:wrap\"></div></div>'")

# 8. Click delegates (dashCards + navLinks)
old_end = "built=true;showSec('dash')}"
deleg = '''if(g('dashCards')&&!g('dashCards').dataset.bound){g('dashCards').dataset.bound='1';g('dashCards').addEventListener('click',function(e){var d=e.target.closest('[data-dash]');if(d){var t=d.getAttribute('data-dash');if(t==='log'){window.__admType='Logiciel';window.__admCat='Tous'}else if(t==='app'){window.__admType='Application';window.__admCat='Tous'}else{window.__admType='Tous';window.__admCat='Tous'}showSec('prods');return}var c=e.target.closest('[data-cat]');if(c){window.__admCat=c.getAttribute('data-cat');window.__admType='Tous';showSec('prods')}})}
if(g('navLinks')&&!g('navLinks').dataset.bound){g('navLinks').dataset.bound='1';g('navLinks').addEventListener('click',function(e){var c=e.target.closest('[data-navcat]');if(c){window.__admCat=c.getAttribute('data-navcat');window.__admType='Tous';showSec('prods')}})}
built=true;showSec('dash')}'''
b = b.replace(old_end, deleg)

open('admin.js', 'w', encoding='utf-8').write(b)
print('OK admin.js v31 - compact + clickable + nav admin-only')
