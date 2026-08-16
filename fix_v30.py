# 1. app1.js : coverHTML -> getImageUrl
a = open('app1.js', encoding='utf-8').read()
a = a.replace("'<img src=\"'+esc(it.image)+'\" alt=\"\" loading=\"lazy\">'",
              "'<img src=\"'+esc(window.getImageUrl?getImageUrl(it.image):it.image)+'\" alt=\"\" loading=\"lazy\">'")
open('app1.js', 'w', encoding='utf-8').write(a)
print('OK app1.js coverHTML')

# 2. admin.js : rows thumb -> getImageUrl
b = open('admin.js', encoding='utf-8').read()
b = b.replace("var thumb=it.image?'<img src=\"'+esc(it.image)+'\" alt=\"\">':",
              "var thumb=it.image?'<img src=\"'+esc(window.getImageUrl?getImageUrl(it.image):it.image)+'\" alt=\"\">':")
open('admin.js', 'w', encoding='utf-8').write(b)
print('OK admin.js rows')

# 3. supa.js : regen marina (DBKEY logiciel_db_v3, auth check, onFileChange upload)
supa = '''(function(){
var URL='https://cshmobqykkqjmusnkeom.supabase.co';
var KEY='sb_publishable_rveJ3wjRsYkcPWYdaPSqJA_RKSiGqDF';
var DBKEY='logiciel_db_v3';
var PROXY=URL+'/functions/v1/tg?p=';
var UP=URL+'/functions/v1/tg-upload';
window.PROXY=PROXY;window.UPLOAD=UP;
window.getImageUrl=function(p){if(!p||p.length<2)return '';if(p.indexOf('http')===0)return p;return PROXY+p;};
window.uploadToTelegram=function(file){var fd=new FormData();fd.append('file',file);return fetch(UP,{method:'POST',body:fd}).then(function(r){return r.json()}).then(function(d){if(!d.ok)throw new Error(d.err||'upload failed');return d.file_path;});};
function hdrs(x){var h={'apikey':KEY,'Content-Type':'application/json'};if(x)for(var k in x)h[k]=x[k];return h}
function clean(p){return{id:p.id,name:p.name,type:p.type||'Logiciel',category:p.category||'Design',os:p.os||'Windows',version:p.version||'',size:p.size||'',dl:p.dl||0,rate:p.rate||4.5,price:p.price||'',image:p.image||'',link:p.link||'',date:p.date||'',info:p.info||'',install:p.install||''}}
var origSet=Storage.prototype.setItem;
window.supaSync=function(cb){if(!window.state||!state.list||!state.list.length){if(cb)cb(false);return}
fetch(URL+'/rest/v1/products?on_conflict=id',{method:'POST',headers:hdrs({'Prefer':'resolution=merge-duplicates','x-admin-key':'LOGIPLUS2026'}),body:JSON.stringify(state.list.map(clean))}).then(function(r){if(!r.ok)return r.text().then(function(t){throw new Error(t)});origSet.call(localStorage,'lg_dirty','0');if(window.toast)toast('Sync Supabase OK ('+state.list.length+')');if(cb)cb(true)}).catch(function(e){if(window.toast)toast('Sync erreur: '+e.message);if(cb)cb(false)});};
Storage.prototype.setItem=function(k,v){var r=origSet.call(this,k,v);
if(k===DBKEY){origSet.call(this,'lg_dirty','1');clearTimeout(window.__st);window.__st=setTimeout(function(){if(window.supaSync)window.supaSync();},2000);}
return r;};
setTimeout(function(){
var local=null;try{local=JSON.parse(localStorage.getItem(DBKEY)||'null')}catch(e){}
var dirty=localStorage.getItem('lg_dirty')==='1';
var auth=window.state&&state.authed;
fetch(URL+'/rest/v1/products?select=*',{headers:hdrs()}).then(function(r){return r.ok?r.json():[]}).then(function(rows){
if(!window.state)return;
if(dirty||(auth&&local&&local.length&&JSON.stringify(local)!==JSON.stringify(rows))){state.list=local&&local.length?local:state.list;window.supaSync();return;}
if(rows&&rows.length){state.list=rows;origSet.call(localStorage,DBKEY,JSON.stringify(rows));if(window.renderGrid)renderGrid();}
}).catch(function(){});
},1500);
window.onFileChange=function(inp){if(!inp.files||!inp.files[0])return;var f=inp.files[0];
if(window.toast)toast('Upload sary any Telegram...');
window.uploadToTelegram(f).then(function(p){var fi=document.getElementById('f-image');if(fi)fi.value=p;var pv=document.getElementById('f-preview');if(pv){pv.hidden=false;var im=pv.querySelector('img');if(im)im.src=window.PROXY+p;}if(window.toast)toast('Sary voatahiry: '+p);}).catch(function(e){if(window.toast)toast('Erreur: '+e.message);});};
var tries=0;var iv=setInterval(function(){tries++;
var auth=window.state&&state.authed;
var v=document.getElementById('view-admin');
if(auth&&v&&!v.hidden&&!document.getElementById('supaBtn')){var b=document.createElement('button');b.id='supaBtn';b.className='btn';b.style.cssText='background:linear-gradient(135deg,#38bdf8,#2563eb);color:#fff;border:none;margin:8px;padding:10px 16px;border-radius:12px;font-weight:700';b.textContent='Sync Supabase';b.onclick=function(){window.supaSync();};v.insertBefore(b,v.firstChild);}
if(!auth){var sb=document.getElementById('supaBtn');if(sb)sb.remove();}
if(tries>60)clearInterval(iv);},700);
})();'''
open('supa.js', 'w', encoding='utf-8').write(supa)
print('OK supa.js v30')
