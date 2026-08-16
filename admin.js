
window.PROXY="https://cshmobqykkqjmusnkeom.supabase.co/functions/v1/tg?p=";
window.UPLOAD="https://cshmobqykkqjmusnkeom.supabase.co/functions/v1/tg-upload";
window.getImageUrl=function(p){if(!p||p.length<2)return "";if(p.startsWith("http"))return p;return window.PROXY+p;};
window.uploadToTelegram=function(file){
  var fd=new FormData();fd.append('file',file);
  return fetch(window.UPLOAD,{method:'POST',body:fd}).then(function(r){return r.json()}).then(function(d){
    if(!d.ok)throw new Error(d.err||"Upload failed");return d.file_path;
  });
};
(function(){
function g(id){return document.getElementById(id)}
var st=document.createElement('style');st.textContent='.adm-menu{display:flex;gap:6px;flex-wrap:nowrap;overflow-x:auto;margin:10px 0;padding-bottom:4px;scrollbar-width:none;-webkit-overflow-scrolling:touch}.adm-menu::-webkit-scrollbar{display:none}.adm-m{padding:7px 12px;flex:none;white-space:nowrap;border-radius:10px;border:1px solid var(--border);background:var(--ghost-bg);color:var(--muted);font-weight:600;font-size:.78rem;cursor:pointer;transition:.2s}.adm-m.active{background:var(--grad);color:#fff;border-color:transparent}.dash-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(86px,1fr));gap:8px}.dash-c{padding:10px 6px;text-align:center;cursor:pointer}.dash-c:active{transform:scale(.96)}.dash-c b{display:block;font-family:Sora;font-size:1.05rem;font-weight:800;background:var(--grad);-webkit-background-clip:text;color:transparent}.dash-c span{color:var(--muted);font-size:.66rem}#adminPanel .btn{padding:8px 13px;font-size:.78rem;border-radius:10px}#adminPanel .panel{padding:12px}';var st2=document.createElement('style');st2.textContent='#view-admin .btn{padding:8px 13px;font-size:.78rem;border-radius:10px;flex:none;white-space:nowrap}#view-admin .adm-sec .btn{padding:8px 13px;font-size:.78rem}';document.head.appendChild(st2);document.head.appendChild(st);
var built=false,cur='dash';
function rows(items){return items.map(function(it){var thumb=it.image?'<img src="'+esc(window.getImageUrl?getImageUrl(it.image):it.image)+'" alt="">':esc(initials(it.name));return '<div class="a-row"><div class="a-thumb cg'+(hashN(it.name)%5)+'">'+thumb+'</div><div class="a-info"><b>'+esc(it.name)+'</b><span>'+esc(it.type||'Logiciel')+' • '+esc(it.os||'—')+' • '+esc(it.category||'Autre')+'</span></div><span class="a-price">'+esc(it.price||'—')+'</span><div class="a-actions"><button data-edit="'+esc(it.id)+'" type="button"><svg class="ni ni-sm"><use href="#i-edit"></use></svg> Modifier</button><button data-del="'+esc(it.id)+'" class="del" type="button"><svg class="ni ni-sm" style="color:#fca5a5;filter:drop-shadow(0 0 4px rgba(244,63,94,.7))"><use href="#i-trash"></use></svg> Suppr.</button></div></div>'}).join('')||'<p style="color:var(--muted)">Aucun produit.</p>'}
function applyCatFilter(){var cat=window.__admCat||'Tous';var typ=window.__admType||'Tous';var q=(g('adminSearch')?g('adminSearch').value:'').toLowerCase();var items=(state.list||[]).filter(function(it){if(typ!=='Tous'&&(it.type||'Logiciel')!==typ)return false;if(cat!=='Tous'&&(it.category||'Autre')!==cat)return false;if(q&&(it.name||'').toLowerCase().indexOf(q)===-1&&(it.category||'').toLowerCase().indexOf(q)===-1)return false;return true});g('listCount').textContent=items.length;g('adminList').innerHTML=rows(items)}
function renderProdsCats(){var host=g('sec-prods');if(!host)return;if(!g('prodCatBar')){var bar=document.createElement('div');bar.id='prodCatBar';bar.className='panel';bar.style.marginBottom='12px';bar.innerHTML='<h3>📂 Filtrer par catégorie</h3><div id="prodCatChips" style="display:flex;gap:8px;flex-wrap:wrap"></div>';host.insertBefore(bar,host.firstChild)}
var cats=['Tous'],seen={};(state.list||[]).forEach(function(i){var c=i.category||'Autre';if(!seen[c]){seen[c]=1;cats.push(c)}});
var curCat=window.__admCat||'Tous';
g('prodCatChips').innerHTML=cats.map(function(c){return '<button data-pc="'+esc(c)+'" style="padding:8px 15px;border-radius:999px;border:1px solid var(--border);background:'+(c===curCat?'var(--grad)':'var(--ghost-bg)')+';color:'+(c===curCat?'#fff':'var(--muted)')+';cursor:pointer;font-size:.82rem;font-weight:600">'+esc(c)+'</button>'}).join('');
g('prodCatChips').onclick=function(e){var b=e.target.closest('[data-pc]');if(!b)return;window.__admCat=b.getAttribute('data-pc');renderProdsCats();applyCatFilter()};
applyCatFilter()}
function renderDash(){var L=state.list||[];var totDl=0;L.forEach(function(i){totDl+=(i.dl||0)});var cats={};L.forEach(function(i){var c=i.category||'Autre';cats[c]=(cats[c]||0)+1});var nbLog=L.filter(function(i){return(i.type||'Logiciel')==='Logiciel'}).length;var top=L.slice().sort(function(a,b){return(b.dl||0)-(a.dl||0)}).slice(0,5);
var html='<div class="panel dash-c" data-dash="all"><b>'+L.length+'</b><span>Produits</span></div><div class="panel dash-c" data-dash="log"><b>'+nbLog+'</b><span>Logiciels</span></div><div class="panel dash-c" data-dash="app"><b>'+(L.length-nbLog)+'</b><span>Applications</span></div><div class="panel dash-c" data-dash="all"><b>'+Object.keys(cats).length+'</b><span>Catégories</span></div><div class="panel dash-c"><b>'+totDl.toLocaleString()+'</b><span>Téléch.</span></div><div class="panel" style="grid-column:1/-1"><h3>🏆 Top 5 téléchargements</h3>'+top.map(function(i){return '<div data-edit="'+esc(i.id)+'" style="display:flex;justify-content:space-between;gap:10px;cursor:pointer;padding:8px 0;border-bottom:1px dashed var(--border);font-size:.88rem"><span style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap">'+esc(i.name)+'</span><b style="color:var(--amber);flex:none">'+(i.dl||0).toLocaleString()+'</b></div>'}).join('')+'</div><div class="panel" style="grid-column:1/-1"><h3>📂 Répartition par catégorie</h3>'+Object.keys(cats).map(function(c){return '<div data-cat="'+esc(c)+'" style="display:flex;justify-content:space-between;padding:8px 0;cursor:pointer;border-bottom:1px dashed var(--border);font-size:.88rem"><span>'+esc(c)+'</span><b>'+cats[c]+'</b></div>'}).join('')+'</div>';
if(g('dashCards'))g('dashCards').innerHTML=html}
function renderNav(){var cats=[],seen={};(state.list||[]).forEach(function(i){var c=i.category||'Autre';if(!seen[c]){seen[c]=1;cats.push(c)}});
var h="<p style='color:var(--muted);font-size:.8rem;margin-bottom:10px'>Navigation rapide (ao anatin'ny admin ihany):</p>";
for(var i=0;i<cats.length;i++){(function(c){h+='<button class="btn ghost" data-navcat="'+esc(c)+'">📂 '+esc(c)+'</button>'})(cats[i])}
h+='<button class="btn ghost" onclick="toggleTheme()">🌓 Clair / Sombre</button><button class="btn ghost" onclick="doLogout()">🚪 Déconnexion</button>';
if(g('navLinks'))g('navLinks').innerHTML=h}
function moveSettings(){var ps=g('paySettings');if(ps&&g('sec-set')&&ps.parentNode!==g('sec-set'))g('sec-set').appendChild(ps)}
function showSec(s){cur=s;var map={dash:'sec-dash',prods:'sec-prods',add:'sec-add',imp:'sec-imp',set:'sec-set',nav:'sec-nav'};for(var k in map){var el=g(map[k]);if(el)el.style.display=(k===s)?'block':'none'}
if(s==='dash')renderDash();if(s==='prods')renderProdsCats();if(s==='nav')renderNav();if(s==='set')moveSettings()}
window.admShow=showSec;
function buildAdmin(){var ap=g('adminPanel');if(!ap||ap.hidden)return;if(built){showSec(cur);return}
var _eb=[].slice.call(ap.querySelectorAll('button,label')).filter(function(x){return x.textContent.indexOf('Exporter')>-1})[0];
if(_eb&&_eb.parentNode&&_eb.parentNode!==ap){var _w=_eb.parentNode;_w.style.cssText+=';display:flex;flex-wrap:nowrap;overflow-x:auto;gap:8px;scrollbar-width:none;-webkit-overflow-scrolling:touch;padding-bottom:4px';}
var menu=document.createElement('div');menu.id='admMenu';menu.className='adm-menu';
menu.innerHTML='<button data-s="dash" class="adm-m active">📊 Dashboard</button><button data-s="prods" class="adm-m">📦 Produits</button><button data-s="add" class="adm-m">➕ Ajouter</button><button data-s="imp" class="adm-m">📥 Import/Export</button><button data-s="set" class="adm-m">💳 Paramètres</button><button data-s="nav" class="adm-m">🔗 Navigation</button>';
ap.insertBefore(menu,ap.children[1]||null);
function wrap(id){var d=document.createElement('div');d.className='adm-sec';d.id=id;d.style.display='none';ap.appendChild(d);return d}
var sDash=wrap('sec-dash'),sProds=wrap('sec-prods'),sAdd=wrap('sec-add'),sImp=wrap('sec-imp'),sSet=wrap('sec-set'),sNav=wrap('sec-nav');
var grid=ap.querySelector('.admin-grid');
if(grid){var form=g('softForm');var listPanel=grid.children[1];if(form)sAdd.appendChild(form);if(listPanel)sProds.appendChild(listPanel);grid.remove()}
var sync=ap.querySelector('.sync-note');if(sync)sImp.appendChild(sync);
sDash.innerHTML='<div class="dash-grid" id="dashCards"></div>';
sNav.innerHTML='<div class="panel"><h3>🔗 Navigation rapide</h3><div id="navLinks" style="display:flex;gap:8px;flex-wrap:wrap"></div></div>';
var imp=document.createElement('div');imp.className='panel';imp.innerHTML='<h3>📥 Importer / 📤 Exporter</h3><p style="color:var(--muted);font-size:.85rem;margin-bottom:12px">Import : fichier JSON (liste produits). Export : alefaso ao amin\'ny dossier <b>data/</b> ny logiciels.json.</p><div style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn ghost" type="button" onclick="doExport()">📤 Exporter logiciels.json</button><label class="btn ghost" style="cursor:pointer">📥 Importer JSON<input id="admImport" type="file" accept=".json" hidden></label></div>';
sImp.appendChild(imp);
imp.querySelector('#admImport').addEventListener('change',function(){doImportChange(this)});
menu.addEventListener('click',function(e){var b=e.target.closest('[data-s]');if(!b)return;var all=menu.querySelectorAll('.adm-m');for(var i=0;i<all.length;i++){all[i].classList.toggle('active',all[i]===b)}showSec(b.getAttribute('data-s'))});
if(g('adminSearch'))g('adminSearch').addEventListener('input',function(){setTimeout(applyCatFilter,0)});
document.addEventListener('click',function(e){if(e.target.closest('[data-edit]')){showSec('add')}});
if(g('dashCards')&&!g('dashCards').dataset.bound){g('dashCards').dataset.bound='1';g('dashCards').addEventListener('click',function(e){var d=e.target.closest('[data-dash]');if(d){var t=d.getAttribute('data-dash');if(t==='log'){window.__admType='Logiciel';window.__admCat='Tous'}else if(t==='app'){window.__admType='Application';window.__admCat='Tous'}else{window.__admType='Tous';window.__admCat='Tous'}showSec('prods');return}var c=e.target.closest('[data-cat]');if(c){window.__admCat=c.getAttribute('data-cat');window.__admType='Tous';showSec('prods')}})}
if(g('navLinks')&&!g('navLinks').dataset.bound){g('navLinks').dataset.bound='1';g('navLinks').addEventListener('click',function(e){var c=e.target.closest('[data-navcat]');if(c){window.__admCat=c.getAttribute('data-navcat');window.__admType='Tous';showSec('prods')}})}
built=true;showSec('dash')}
setInterval(function(){var ap=g('adminPanel');if(ap&&!ap.hidden){buildAdmin();if(cur==='set')moveSettings();if(cur==='dash')renderDash()}},700);
})();
