import re
old = ''
try:
    old = open('supa.js', encoding='utf-8').read()
except Exception:
    pass
mk = re.search(r"var KEY='([^']*)'", old)
KEY = mk.group(1) if mk else 'sb_publishable_rveJ3wjRsYkcPWYdaPSqJA_RKSiGqDF'
ma = re.search(r"var DBKEY='([^']*)'", old)
a1 = open('app1.js', encoding='utf-8').read()
md = re.search(r"localStorage\.(?:get|set)Item\(['\"]([^'\"]+)['\"]", a1)
DBKEY = ma.group(1) if ma else (md.group(1) if md else 'lg_db')

supa = '''(function(){
var URL='https://cshmobqykkqjmusnkeom.supabase.co';
var KEY='__KEY__';
var DBKEY='__DBKEY__';
var PROXY='https://cshmobqykkqjmusnkeom.supabase.co/functions/v1/tg?p=';
var UP='https://cshmobqykkqjmusnkeom.supabase.co/functions/v1/tg-upload';
window.PROXY=PROXY;window.UPLOAD=UP;
window.getImageUrl=function(p){if(!p||p.length<2)return '';if(p.indexOf('http')===0)return p;return PROXY+p;};
window.uploadToTelegram=function(file){var fd=new FormData();fd.append('file',file);return fetch(UP,{method:'POST',body:fd}).then(function(r){return r.json()}).then(function(d){if(!d.ok)throw new Error(d.err||'upload failed');return d.file_path;});};
function hdrs(x){var h={'apikey':KEY,'Content-Type':'application/json'};if(x)for(var k in x)h[k]=x[k];return h}
function clean(p){return{id:p.id,name:p.name,type:p.type||'Logiciel',category:p.category||'Design',os:p.os||'Windows',version:p.version||'',size:p.size||'',dl:p.dl||0,rate:p.rate||4.5,price:p.price||'',image:p.image||'',link:p.link||'',date:p.date||'',info:p.info||'',install:p.install||''}}
var origSet=Storage.prototype.setItem;
var origGet=function(k){try{return localStorage.getItem(k)}catch(e){return null}};
window.supaSync=function(cb){if(!window.state||!state.list||!state.list.length){if(cb)cb(false);return}
fetch(URL+'/rest/v1/products?on_conflict=id',{method:'POST',headers:hdrs({'Prefer':'resolution=merge-duplicates','x-admin-key':'LOGIPLUS2026'}),body:JSON.stringify(state.list.map(clean))}).then(function(r){if(!r.ok)return r.text().then(function(t){throw new Error(t)});origSet.call(localStorage,'lg_dirty','0');if(window.toast)toast('Sync Supabase OK ('+state.list.length+')');if(cb)cb(true)}).catch(function(e){if(window.toast)toast('Sync erreur: '+e.message);if(cb)cb(false)})};
Storage.prototype.setItem=function(k,v){var r=origSet.call(this,k,v);
if(k===DBKEY){origSet.call(this,'lg_dirty','1');clearTimeout(window.__st);window.__st=setTimeout(function(){if(window.supaSync)window.supaSync()},2000)}
return r};
setTimeout(function(){
var dirty=origGet('lg_dirty')==='1';
if(dirty){if(window.supaSync)window.supaSync();return}
fetch(URL+'/rest/v1/products?select=*',{headers:hdrs()}).then(function(r){return r.ok?r.json():[]}).then(function(rows){if(rows&&rows.length&&window.state){state.list=rows;origSet.call(localStorage,DBKEY,JSON.stringify(rows));if(window.renderGrid)renderGrid()}}).catch(function(){});
},1500);
var tries=0;var iv=setInterval(function(){tries++;
var v=document.getElementById('view-admin');
if(v&&!v.hidden){
if(!document.getElementById('supaBtn')){var b=document.createElement('button');b.id='supaBtn';b.className='btn';b.style.cssText='background:linear-gradient(135deg,#38bdf8,#2563eb);color:#fff;border:none;margin:8px;padding:10px 16px;border-radius:12px;font-weight:700';b.textContent='Sync Supabase';b.onclick=function(){window.supaSync()};v.insertBefore(b,v.firstChild)}
if(!document.getElementById('tgUpBtn')){var u=document.createElement('button');u.id='tgUpBtn';u.style.cssText='position:fixed;right:14px;bottom:90px;z-index:999;background:#2563eb;color:#fff;border:none;border-radius:30px;padding:12px 16px;font-weight:700;box-shadow:0 6px 18px rgba(0,0,0,.35)';u.textContent='Sary Telegram';u.onclick=function(){var i=document.createElement('input');i.type='file';i.accept='image/*';i.onchange=function(){if(!i.files[0])return;if(window.toast)toast('Upload sary...');window.uploadToTelegram(i.files[0]).then(function(p){if(window.toast)toast('OK '+p);try{navigator.clipboard.writeText(p)}catch(e){}var ins=document.querySelectorAll('input[id*="image"],input[name*="image"],input[placeholder*="image"],input[id*="img"],input[name*="img"]');for(var k=0;k<ins.length;k++)ins[k].value=p}).catch(function(e){if(window.toast)toast('Erreur: '+e.message)})};i.click()};v.appendChild(u)}
}
if(tries>40)clearInterval(iv)},700);
})();'''.replace('__KEY__', KEY).replace('__DBKEY__', DBKEY)
open('supa.js', 'w', encoding='utf-8').write(supa)
print('OK supa.js v29 - auto-sync + upload button')
