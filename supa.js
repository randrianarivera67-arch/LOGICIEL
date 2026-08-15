(function(){
var URL='https://cshmobqykkqjmusnkeom.supabase.co';
var KEY='sb_publis...key-nao...';
var DBKEY='lg_db';
function hdrs(x){var h={'apikey':KEY,'Content-Type':'application/json'};if(x)for(var k in x)h[k]=x[k];return h}
function clean(p){return{id:p.id,name:p.name,type:p.type||'Logiciel',category:p.category||'Design',os:p.os||'Windows',version:p.version||'',size:p.size||'',dl:p.dl||0,rate:p.rate||4.5,price:p.price||'',image:p.image||'',link:p.link||'',date:p.date||'',info:p.info||'',install:p.install||''}}
window.supaSync=function(){if(!window.state||!state.list||!state.list.length){toast('Aucun produit a synchroniser');return}
fetch(URL+'/rest/v1/products?on_conflict=id',{method:'POST',headers:hdrs({'Prefer':'resolution=merge-duplicates','x-admin-key':'LOGIPLUS2026'}),body:JSON.stringify(state.list.map(clean))}).then(function(r){if(!r.ok)return r.text().then(function(t){throw new Error(t)});try{localStorage.setItem(DBKEY,JSON.stringify(state.list))}catch(e){}toast('Sync Supabase OK ('+state.list.length+' produits)')}).catch(function(e){toast('Sync erreur: '+e.message)})};
setTimeout(function(){fetch(URL+'/rest/v1/products?select=*',{headers:hdrs()}).then(function(r){return r.ok?r.json():[]}).then(function(rows){if(rows&&rows.length&&window.state){state.list=rows;try{localStorage.setItem(DBKEY,JSON.stringify(rows))}catch(e){}if(window.renderGrid)renderGrid()}}).catch(function(){})},1200);
var tries=0;var iv=setInterval(function(){tries++;var v=document.getElementById('view-admin');if(v&&!document.getElementById('supaBtn')){var b=document.createElement('button');b.id='supaBtn';b.className='btn';b.style.cssText='background:linear-gradient(135deg,#38bdf8,#2563eb);color:#fff;border:none;margin:8px;padding:10px 16px;border-radius:12px;font-weight:700';b.textContent='Sync Supabase';b.onclick=window.supaSync;v.insertBefore(b,v.firstChild)}if(tries>30)clearInterval(iv)},700);
})();