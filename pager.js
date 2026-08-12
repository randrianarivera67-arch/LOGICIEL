(function(){
var PAGE=8,visible=PAGE;
function cardHTML(it,i){var type=it.type||'Logiciel';var os=osInfo(it.os);return '<article class="card" data-open="'+esc(it.id)+'" style="animation-delay:'+(i%PAGE)*40+'ms"><div class="c-top"><div class="c-icon"><span class="t-badge tb-'+esc(type)+'">'+esc(type)+'</span>'+coverHTML(it)+'<span class="p-badge">'+esc(it.price||'—')+'</span></div><div class="c-head"><h3>'+esc(it.name)+(it.version?' '+esc(it.version):'')+'</h3><p class="c-desc">'+esc(it.info||'')+'</p><span class="c-cat">'+esc(it.category||'Autre')+'</span></div></div><div class="c-mid"><span class="c-os"><svg class="ni ni-sm" style="color:'+os.c+';filter:none"><use href="'+os.ic+'"></use></svg>'+esc(it.os||'Autre')+'</span><span class="c-dl"><svg class="ni ni-sm" style="color:var(--muted);filter:none"><use href="#i-cloud-dl"></use></svg>'+esc(it.dl||0)+'</span></div><div class="c-bot"><div class="c-rep"><span>Reputation</span><div class="stars">'+starsHTML(it.rate)+'</div></div><div class="c-size">'+fmtSize(it.size)+'</div></div></article>'}
window.renderGrid=function(){
var items=filtered();renderStats();
gid('resultInfo').textContent=items.length+' résultat'+(items.length>1?'s':'');
gid('empty').hidden=items.length>0;
var title=state.cat!=='Tous'?state.cat:(state.type==='Tous'?'Tous les produits':(state.type==='Logiciel'?'Windows & Logiciels':'Applications'));
gid('listTitle').textContent=title;
var shown=items.slice(0,visible);
gid('grid').innerHTML=shown.map(cardHTML).join('');
var more=items.length-visible;
var btn=gid('loadMore');
if(!btn){btn=document.createElement('button');btn.id='loadMore';btn.type='button';btn.className='btn ghost';btn.style.cssText='display:block;margin:6px auto 46px;padding:12px 34px';btn.onclick=function(){visible+=PAGE;window.renderGrid()};gid('grid').parentNode.insertBefore(btn,gid('grid').nextSibling)}
if(more>0){btn.hidden=false;btn.textContent='Voir plus ('+more+' restants) ↓'}else{btn.hidden=true}
};
document.addEventListener('input',function(e){if(e.target&&e.target.id==='search'){visible=PAGE}},true);
document.addEventListener('click',function(e){if(e.target&&(e.target.closest('.seg button')||e.target.closest('[data-cat]')||e.target.closest('.btn-va'))){visible=PAGE}},true);
})();
