(function(){
function type(el,txt,sp){if(!el)return;var i=0;el.classList.add('tw2');(function t(){i++;el.textContent=txt.slice(0,i);if(i<txt.length)setTimeout(t,sp||55)})()}
function start(){
if(document.getElementById('intro'))return;
var ov=document.createElement('div');ov.id='intro';
ov.innerHTML='<button class="skip" id="iSkip">Passer ›</button>'
+'<div class="iscene" id="sc1"><svg class="ilogo" viewBox="0 0 48 48" fill="none"><path d="M6 15 L30 6 L30 15 L6 24 Z" fill="#38bdf8"/><path d="M10 26 L34 17 L34 26 L10 35 Z" fill="#f43f5e"/><path d="M14 37 L38 28 L38 37 L14 46 Z" fill="#8b5cf6"/></svg><h2 id="tw1"></h2><p>La plateforme premium des logiciels & applications</p></div>'
+'<div class="iscene" id="sc2"><img class="iimg" src="img/hero.png" alt="" onerror="this.style.display=\'none\'"><h2 id="tw2b"></h2><p>Sans compte. Sans attente.</p></div>'
+'<div class="iscene" id="sc3"><h2>Tout ce qu\'il vous faut</h2><div class="ifeats"><div class="ifeat"><b>💳</b>Orange Money, M\'Vola, Airtel, PayPal</div><div class="ifeat"><b>⚡</b>Téléchargement instantané</div><div class="ifeat"><b>🛒</b>Panier & liens sécurisés</div><div class="ifeat"><b>🕐</b>Support client 24/7</div></div></div>'
+'<div class="iscene" id="sc4"><h2>Prêt à commencer ?</h2><button class="icta" id="iGo">Découvrir Logiplus+ →</button></div>'
+'<div class="bar" id="iBar"></div>';
document.body.appendChild(ov);
var t0=Date.now(),total=12500;
var barI=setInterval(function(){var p=Math.min(100,(Date.now()-t0)/total*100);var b=document.getElementById('iBar');if(b)b.style.width=p+'%';if(p>=100)finish()},100);
function show(id){var s=['sc1','sc2','sc3','sc4'];for(var i=0;i<s.length;i++){var e=document.getElementById(s[i]);if(e)e.classList.toggle('on',s[i]===id)}}
function finish(){clearInterval(barI);var e=document.getElementById('intro');if(e)e.remove();try{localStorage.setItem('lg_intro_seen','1')}catch(err){}}
document.getElementById('iSkip').onclick=finish;
document.getElementById('iGo').onclick=finish;
show('sc1');type(document.getElementById('tw1'),'Logiplus+');
setTimeout(function(){show('sc2');type(document.getElementById('tw2b'),'Recherchez. Cliquez. Téléchargez.')},2800);
setTimeout(function(){show('sc3');var f=document.querySelectorAll('.ifeat');for(var i=0;i<f.length;i++){(function(el,d){setTimeout(function(){el.classList.add('on')},d)})(f[i],i*350)}},6000);
setTimeout(function(){show('sc4')},9500);
setTimeout(finish,total+300);
}
var seen=null;try{seen=localStorage.getItem('lg_intro_seen')}catch(e){}
if(seen!=='1'){setTimeout(start,400)}
window.replayIntro=function(){start()};
var fc=document.querySelector('footer .container');
if(fc){var a=document.createElement('a');a.href='#';a.style.cursor='pointer';a.textContent='▶ Intro';a.onclick=function(e){e.preventDefault();start()};fc.appendChild(a)}
})();
