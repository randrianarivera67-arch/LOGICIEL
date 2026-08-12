import re

css = '''.stage{position:relative;max-width:860px;margin:0 auto 26px;height:360px;border-radius:24px;border:1px solid var(--border);background:var(--panel);overflow:hidden;backdrop-filter:blur(10px)}
@media(max-width:640px){.stage{height:340px}}
.sbar{position:absolute;left:0;bottom:0;height:3px;width:100%;background:rgba(255,255,255,.06);z-index:4}
.sbar i{display:block;height:100%;width:0;background:var(--grad)}
.iscene{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:20px;opacity:0;transform:scale(.97);transition:opacity .7s,transform .7s;text-align:center}
.iscene.on{opacity:1;transform:scale(1)}
.iscene h2{font-family:Sora,sans-serif;font-size:clamp(1.4rem,4vw,2.4rem);font-weight:800}
.iscene p{color:var(--muted);font-size:.92rem;max-width:520px}
.ilogo{width:64px;height:64px}
.iimg{max-height:210px;max-width:78%;border-radius:16px;border:1px solid var(--border);box-shadow:0 30px 70px -25px rgba(37,99,235,.55)}
.chat-b{position:absolute;background:var(--panel-strong);border:1px solid var(--border);border-radius:14px;padding:9px 13px;font-size:.78rem;max-width:70%;box-shadow:0 10px 30px -10px rgba(0,0,0,.5);animation:popIn .5s both;text-align:left}
.chat-b .who{display:block;font-size:.6rem;font-weight:800;margin-bottom:3px;text-transform:uppercase;letter-spacing:.08em;color:var(--ni-color)}
.chat-b.client{right:5%;top:8%;border-bottom-right-radius:4px}
.chat-b.agent{left:5%;bottom:10%;border-bottom-left-radius:4px;border-color:rgba(45,212,191,.45)}
.chat-b.agent .who{color:var(--teal)}
@keyframes popIn{from{opacity:0;transform:scale(.85) translateY(10px)}to{opacity:1;transform:scale(1) translateY(0)}}
.typing{display:inline-flex;gap:4px}
.typing i{width:6px;height:6px;border-radius:50%;background:var(--muted);animation:tp 1s infinite}
.typing i:nth-child(2){animation-delay:.2s}
.typing i:nth-child(3){animation-delay:.4s}
@keyframes tp{0%,100%{opacity:.3;transform:translateY(0)}50%{opacity:1;transform:translateY(-3px)}}
.ifeats{display:flex;gap:12px;flex-wrap:wrap;justify-content:center}
.ifeat.pay{display:flex;flex-direction:column;align-items:center;gap:8px;padding:12px 16px;border-radius:16px;border:1px solid var(--border);background:var(--ghost-bg);font-size:.78rem;font-weight:600;opacity:0;transform:translateY(12px);transition:.5s}
.ifeat.pay.on{opacity:1;transform:translateY(0)}
.ifeat.pay img{width:44px;height:44px;border-radius:10px;object-fit:cover}
.tw2::after{content:'';display:inline-block;width:2px;height:1em;background:var(--ni-color);vertical-align:-2px;margin-left:3px;animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}'''

js = '''(function(){
var scenes=['sc1','sc2','sc3','sc4'];
var durs=[3000,4600,4600,3000];
var total=durs[0]+durs[1]+durs[2]+durs[3];
var idx=0,t0=Date.now(),s0=t0;
function type(el,txt){if(!el)return;el.textContent='';var i=0;el.classList.add('tw2');(function t(){i++;el.textContent=txt.slice(0,i);if(i<txt.length)setTimeout(t,60)})()}
var chatOn=false;
function startChat(){if(chatOn)return;chatOn=true;var box=document.getElementById('chatLoop');if(!box)return;var msgs=['Bonjour ! Photoshop 2026 est disponible ✓','Paiement M\\'Vola confirmé — lien envoyé 🚀','Besoin d\\'aide ? Agent disponible 24/7 💬'];var mi=0;(function loop(){box.innerHTML='<span class="who">Agent Logiplus+</span><span class="typing"><i></i><i></i><i></i></span>';setTimeout(function(){box.innerHTML='<span class="who">Agent Logiplus+</span>'+msgs[mi%msgs.length];mi++;setTimeout(loop,3200)},1000)})();}
function show(i){for(var k=0;k<scenes.length;k++){var e=document.getElementById(scenes[k]);if(e)e.classList.toggle('on',k===i)}
if(i===0)type(document.getElementById('tw1'),'Logiplus+');
if(i===1)startChat();
if(i===2){var f=document.querySelectorAll('.ifeat.pay');for(var j=0;j<f.length;j++){(function(el,d){setTimeout(function(){el.classList.add('on')},d)})(f[j],j*250)}}
if(i===3)type(document.getElementById('tw4'),'Prêt à commencer ?');}
setInterval(function(){var now=Date.now();if(now-s0>durs[idx]){s0=now;idx=(idx+1)%scenes.length;show(idx)}var el=(now-t0)%total;var b=document.getElementById('stageBar');if(b)b.style.width=(el/total*100)+'%'},120);
show(0);
})();'''

new_hero = '''<div class="hero">
<div class="stage" id="stage">
<div class="sbar"><i id="stageBar"></i></div>
<div class="iscene on" id="sc1"><svg class="ilogo" viewBox="0 0 48 48" fill="none"><path d="M6 15 L30 6 L30 15 L6 24 Z" fill="#38bdf8"/><path d="M10 26 L34 17 L34 26 L10 35 Z" fill="#f43f5e"/><path d="M14 37 L38 28 L38 37 L14 46 Z" fill="#8b5cf6"/></svg><h2 id="tw1">Logiplus+</h2><p>La plateforme premium des logiciels & applications</p></div>
<div class="iscene" id="sc2"><img class="iimg" src="img/hero.png" alt="Client et agent Logiplus+" onerror="this.style.display='none'"><div class="chat-b client"><span class="who">Client</span>Bonjour ! Je cherche un logiciel de design 🎨</div><div class="chat-b agent" id="chatLoop"><span class="who">Agent Logiplus+</span>Bonjour ! Photoshop 2026 est disponible ✓</div></div>
<div class="iscene" id="sc3"><h2>Moyens de paiement sécurisés</h2><div class="ifeats"><div class="ifeat pay"><img src="img/orange.png" alt="" onerror="this.style.display='none'"><span>Orange Money</span></div><div class="ifeat pay"><img src="img/mvola.png" alt="" onerror="this.style.display='none'"><span>M'Vola</span></div><div class="ifeat pay"><img src="img/airtel.png" alt="" onerror="this.style.display='none'"><span>Airtel Money</span></div><div class="ifeat pay"><img src="img/paypal.png" alt="" onerror="this.style.display='none'"><span>PayPal</span></div></div><p>⚡ Téléchargement instantané • 🕐 Support 24/7</p></div>
<div class="iscene" id="sc4"><h2 id="tw4">Prêt à commencer ?</h2><p>Recherchez, cliquez, téléchargez — sans compte requis.</p></div>
</div>
<div class="search"><svg class="ni ni-sm"><use href="#i-search"></use></svg><input id="search" type="search" placeholder="Rechercher un logiciel ou une application…" autocomplete="off"><kbd>/</kbd></div>
<div class="stats">
<div><b id="statCount">0</b><span>Produits disponibles</span></div>
<div><b id="statLog">0</b><span>Logiciels</span></div>
<div><b id="statApp">0</b><span>Applications</span></div>
</div>
</div>
'''

open('hero.css','w',encoding='utf-8').write(css)
open('hero.js','w',encoding='utf-8').write(js)
c = open('index.html', encoding='utf-8').read()
m = re.search(r'<div class="hero">.*?(<div class="toolbar">)', c, flags=re.S)
if m:
    c2 = c[:m.start()] + new_hero + c[m.start(1):]
    open('index.html','w',encoding='utf-8').write(c2)
    print('OK - hero vidéo installé, chaos voafafa')
else:
    print('ECHEC - tsy hita ny hero')
