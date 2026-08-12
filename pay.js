(function(){
function g(id){return document.getElementById(id)}
function escS(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function pget(k,d){try{var v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}}
function pset(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
var SETTINGS=pget('lg_settings',{orange:'032 XX XXX XX',mvola:'070 XX XXX XX',airtel:'033 XX XXX XX',paypal:'paypal.me/logiciel'});
var CART=pget('lg_cart',[]);
var fab=document.createElement('button');fab.className='pm-fab';fab.onclick=openDrawer;fab.innerHTML='<svg class="ni"><use href="#i-cart"></use></svg><span class="pm-count" id="cartCount">0</span>';document.body.appendChild(fab);
var dr=document.createElement('div');dr.className='drawer';dr.innerHTML='<div class="drawer-h"><h3 style="font-family:Sora">🛒 Mes achats</h3><button class="btn ghost" style="padding:8px 14px" onclick="closeDrawer()">✕</button></div><div class="drawer-b" id="drawerBody"></div>';document.body.appendChild(dr);
window.closeDrawer=function(){dr.classList.remove('open')};
function openDrawer(){renderDrawer();dr.classList.add('open')}
function renderDrawer(){g('cartCount').textContent=CART.length;if(!CART.length){g('drawerBody').innerHTML='<p style="color:var(--muted);text-align:center;padding:30px 0">Aucun achat.<br>Cliquez « Acheter » sur un produit.</p>';return}
g('drawerBody').innerHTML=CART.map(function(c){return '<div class="dw-item"><div class="dw-info"><b>'+escS(c.name)+'</b><span>'+escS(c.method)+' • Réf : '+escS(c.ref)+'</span></div><a class="dw-dl" href="'+escS(c.link)+'" target="_blank" rel="noopener">Télécharger</a></div>'}).join('')}
var METHODS=[
{id:'orange',name:'Orange Money',img:'img/orange.png',fb:'#f97316',key:'orange'},
{id:'mvola',name:"M'Vola",img:'img/mvola.png',fb:'#eab308',key:'mvola'},
{id:'airtel',name:'Airtel Money',img:'img/airtel.png',fb:'#dc2626',key:'airtel'},
{id:'paypal',name:'PayPal',img:'img/paypal.png',fb:'#2563eb',key:'paypal'}];
var ov=null,curItem=null,curMethod=null;
window.closePay=function(){if(ov){ov.remove();ov=null}}
function logoHTML(m){return '<img src="'+m.img+'" alt="" style="width:56px;height:56px;border-radius:12px;object-fit:cover" onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'grid\'"><div class="pm-fb" style="background:'+m.fb+';display:none">'+m.name+'</div>'}
function openPay(item){curItem=item;curMethod=null;closePay();ov=document.createElement('div');ov.className='modal-ov';ov.innerHTML='<div class="modal" id="pmModal"></div>';document.body.appendChild(ov);renderMethods()}
function renderMethods(){var mh='';for(var i=0;i<METHODS.length;i++){var m=METHODS[i];mh+='<div class="pm-m" data-m="'+m.id+'">'+logoHTML(m)+'<span>'+m.name+'</span></div>'}
g('pmModal').innerHTML='<h3 style="font-family:Sora">💳 Paiement — '+escS(curItem.name)+'</h3><p style="color:var(--amber);font-family:Sora;font-weight:800;font-size:1.2rem;margin:6px 0">'+escS(curItem.price||'—')+'</p><p style="color:var(--muted);font-size:.84rem">Safidio ny fomba fandoavana :</p><div class="pm-methods">'+mh+'</div><button class="btn ghost big" style="margin-top:4px" onclick="closePay()">Annuler</button>';
var els=g('pmModal').querySelectorAll('[data-m]');for(var j=0;j<els.length;j++){(function(el){el.onclick=function(){var id=el.getAttribute('data-m');for(var k=0;k<METHODS.length;k++){if(METHODS[k].id===id){renderPay(METHODS[k]);break}}}})(els[j])}}
function renderPay(m){curMethod=m.id;var num=SETTINGS[m.key]||'—';var isP=m.id==='paypal';
g('pmModal').innerHTML='<button class="btn ghost" style="padding:8px 14px;margin-bottom:14px" onclick="pmBack()">← Changer de méthode</button><div style="display:flex;align-items:center;gap:14px;margin-bottom:12px">'+logoHTML(m)+'<div><b style="font-family:Sora;font-size:1.05rem">'+m.name+'</b><p style="color:var(--amber);font-family:Sora;font-weight:800;font-size:1.15rem;margin:2px 0 0">'+escS(curItem.price||'—')+'</p></div></div><div class="pm-box">'+(isP?'Envoyez le montant à l\'adresse PayPal :':'Envoyez <b>'+escS(curItem.price||'')+'</b> au numéro :')+'<br><span class="pm-num">'+escS(num)+'</span><br>Puis entrez ci-dessous la référence de la transaction.</div><label style="display:block;margin:10px 0 0;font-size:.82rem;color:var(--muted)">Référence transaction<input id="pmRef" placeholder="Ex : 123456789"></label><label style="display:block;margin:8px 0 0;font-size:.82rem;color:var(--muted)">Votre numéro (nandefasana)<input id="pmFrom" placeholder="Ex : 034 …"></label><button class="btn primary big" style="margin-top:12px" onclick="confirmPay()">✅ J\'ai payé — Confirmer</button>'}
window.pmBack=function(){renderMethods()};
window.confirmPay=function(){var ref=g('pmRef')?(g('pmRef').value||'').trim():'';if(!ref){toast('Saisissez la référence de transaction');return}
var m=null;for(var i=0;i<METHODS.length;i++){if(METHODS[i].id===curMethod){m=METHODS[i];break}}
toast('Vérification du paiement…');
setTimeout(function(){CART.unshift({id:curItem.id,name:curItem.name,link:curItem.link,price:curItem.price,method:m.name,ref:ref,date:new Date().toISOString().slice(0,10)});pset('lg_cart',CART);closePay();openDrawer();toast('Paiement confirmé ✓')},1200)};
document.addEventListener('click',function(e){var a=e.target.closest('.d-actions a.btn.primary');if(!a)return;var id=location.hash.slice(11);var it=null;if(window.state){for(var i=0;i<state.list.length;i++){if(state.list[i].id===id){it=state.list[i];break}}}if(!it)return;e.preventDefault();e.stopPropagation();openPay(it)},true);
function injectSettings(){var ap=g('adminPanel');if(!ap||ap.hidden||g('paySettings'))return;var d=document.createElement('div');d.className='panel';d.id='paySettings';d.style.marginTop='22px';
d.innerHTML='<h3>💳 Paramètres de paiement</h3><label>Numéro Orange Money<input id="set-orange"></label><label>Numéro M\'Vola (Telma)<input id="set-mvola"></label><label>Numéro Airtel Money<input id="set-airtel"></label><label>Adresse PayPal<input id="set-paypal"></label><div style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn primary" type="button" onclick="saveSettings()">💾 Enregistrer</button><button class="btn ghost" type="button" onclick="exportSettings()"><svg class="ni ni-sm"><use href="#i-export"></use></svg> settings.json</button></div><p style="color:var(--muted);font-size:.76rem;margin-top:10px">💡 Alefaso ao amin\'ny dossier <b>data/</b> ny settings.json voadika mba ho hitan\'ny client ny numéro.</p>';
ap.appendChild(d);injectSettingsValues()}
function injectSettingsValues(){if(!g('set-orange'))return;g('set-orange').value=SETTINGS.orange||'';g('set-mvola').value=SETTINGS.mvola||'';g('set-airtel').value=SETTINGS.airtel||'';g('set-paypal').value=SETTINGS.paypal||''}
window.saveSettings=function(){SETTINGS={orange:(g('set-orange').value||'').trim(),mvola:(g('set-mvola').value||'').trim(),airtel:(g('set-airtel').value||'').trim(),paypal:(g('set-paypal').value||'').trim()};pset('lg_settings',SETTINGS);toast('Paramètres enregistrés ✓')};
window.exportSettings=function(){var blob=new Blob([JSON.stringify(SETTINGS,null,2)],{type:'application/json'});var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='settings.json';document.body.appendChild(a);a.click();a.remove();toast('settings.json exporté ⬇️')};
fetch('data/settings.json',{cache:'no-store'}).then(function(r){return r.ok?r.json():null}).then(function(j){if(j){if(j.orange)SETTINGS.orange=j.orange;if(j.mvola)SETTINGS.mvola=j.mvola;if(j.airtel)SETTINGS.airtel=j.airtel;if(j.paypal)SETTINGS.paypal=j.paypal;injectSettingsValues()}}).catch(function(){});
window.addEventListener('hashchange',function(){setTimeout(injectSettings,300)});
setTimeout(function(){renderDrawer();injectSettings()},600);
})();
