css = '''.stage-kicker{font-family:Sora,sans-serif;font-weight:700;font-size:clamp(.62rem,2.7vw,1.3rem);color:var(--text);margin:4px auto 16px;max-width:920px;text-align:center;letter-spacing:.02em;white-space:nowrap}
.kstar{width:1em;height:1em;vertical-align:-2px;filter:drop-shadow(0 0 6px rgba(251,191,36,.8))}
.stage{position:relative;max-width:860px;margin:0 auto 26px;height:380px;border-radius:24px;border:1px solid var(--border);overflow:hidden;background:#05070f}
.stage::after{content:'';position:absolute;inset:-6%;background:url("img/stage-bg.png") center/cover no-repeat;animation:kb 26s ease-in-out infinite alternate;z-index:0}
@keyframes kb{from{transform:scale(1) translate(0,0)}to{transform:scale(1.14) translate(-2%,2%)}}
.stage::before{content:'';position:absolute;inset:0;z-index:1;background:linear-gradient(120deg,rgba(56,189,248,.2),rgba(244,63,94,.14),rgba(139,92,246,.22),rgba(45,212,191,.18));background-size:300% 300%;animation:gradMove 12s ease infinite;mix-blend-mode:screen}
body.light .stage::before{mix-blend-mode:multiply;background:linear-gradient(120deg,rgba(2,6,23,.6),rgba(15,23,42,.5),rgba(2,6,23,.6));background-size:300% 300%}
@keyframes gradMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.vig{position:absolute;inset:0;z-index:2;background:radial-gradient(90% 75% at 50% 50%,rgba(2,6,23,.66),rgba(2,6,23,.4) 65%,rgba(2,6,23,.18));pointer-events:none}
@media(max-width:640px){.stage{height:360px}}
.iscene{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:20px;opacity:0;transform:scale(.97);transition:opacity .7s,transform .7s;text-align:center;z-index:3}
.iscene.on{opacity:1;transform:scale(1)}
.iscene h2{font-family:Sora,sans-serif;font-size:clamp(1.4rem,4vw,2.4rem);font-weight:800;color:#fff;text-shadow:0 2px 8px rgba(0,0,0,.9),0 6px 30px rgba(0,0,0,.8)}
.iscene p{color:#f1f5f9;font-size:.95rem;font-weight:600;max-width:520px;text-shadow:0 2px 8px rgba(0,0,0,.9),0 4px 20px rgba(0,0,0,.7)}
.ilogo{width:64px;height:64px;filter:drop-shadow(0 0 18px rgba(56,189,248,.8))}
.s2row{display:flex;align-items:center;gap:20px;justify-content:center}
.iimg{max-height:230px;max-width:44%;border-radius:16px;border:1px solid rgba(255,255,255,.2);box-shadow:0 30px 70px -25px rgba(37,99,235,.65)}
@media(max-width:640px){.s2row .iimg{display:none}}
.phone{position:relative;width:180px;height:300px;border-radius:26px;border:2px solid rgba(255,255,255,.28);background:rgba(5,8,15,.92);box-shadow:0 20px 60px -20px rgba(0,0,0,.85),0 0 30px rgba(56,189,248,.3);overflow:hidden;display:flex;flex-direction:column;flex:none}
.phone::before{content:'';position:absolute;top:6px;left:50%;transform:translateX(-50%);width:64px;height:10px;border-radius:999px;background:#000;z-index:2}
.ph-head{padding:20px 10px 6px;text-align:center;font-size:.6rem;font-weight:800;color:#7dd3fc;text-transform:uppercase;letter-spacing:.08em}
.ph-body{flex:1;padding:8px;display:flex;flex-direction:column;gap:6px;overflow:hidden}
.msg{max-width:88%;padding:7px 9px;border-radius:10px;font-size:.62rem;line-height:1.4;animation:popIn .4s both;text-shadow:none}
.msg.client{align-self:flex-end;background:linear-gradient(135deg,#2563eb,#38bdf8);color:#fff;border-bottom-right-radius:3px}
.msg.agent{align-self:flex-start;background:rgba(255,255,255,.09);border:1px solid rgba(45,212,191,.4);color:#e8ecf8;border-bottom-left-radius:3px}
@keyframes popIn{from{opacity:0;transform:scale(.85) translateY(10px)}to{opacity:1;transform:scale(1) translateY(0)}}
.typing{display:inline-flex;gap:4px}
.typing i{width:6px;height:6px;border-radius:50%;background:#93a0b8;animation:tp 1s infinite}
.typing i:nth-child(2){animation-delay:.2s}
.typing i:nth-child(3){animation-delay:.4s}
@keyframes tp{0%,100%{opacity:.3;transform:translateY(0)}50%{opacity:1;transform:translateY(-3px)}}
.ifeats{display:flex;gap:12px;flex-wrap:wrap;justify-content:center}
.ifeat.pay{display:flex;flex-direction:column;align-items:center;gap:8px;padding:12px 16px;border-radius:16px;border:1px solid rgba(255,255,255,.18);background:rgba(5,8,15,.78);color:#e8ecf8;font-size:.78rem;font-weight:600;opacity:0;transform:translateY(12px);transition:.5s}
.ifeat.pay.on{opacity:1;transform:translateY(0)}
.ifeat.pay img{width:44px;height:44px;border-radius:10px;object-fit:cover}
.tw2::after{content:'';display:inline-block;width:2px;height:1em;background:#7dd3fc;vertical-align:-2px;margin-left:3px;animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
.spark{position:absolute;width:6px;height:6px;border-radius:50%;background:#fff;opacity:0;animation:spop linear infinite;z-index:2;box-shadow:0 0 8px 2px rgba(255,255,255,.5)}
.spark:nth-child(3n){background:#38bdf8;box-shadow:0 0 10px 3px rgba(56,189,248,.6)}
.spark:nth-child(3n+1){background:#f43f5e;box-shadow:0 0 10px 3px rgba(244,63,94,.6)}
.spark:nth-child(3n+2){background:#8b5cf6;box-shadow:0 0 10px 3px rgba(139,92,246,.6)}
@keyframes spop{0%{transform:scale(0);opacity:0}20%{opacity:1}50%{transform:scale(1.5);opacity:.9}100%{transform:scale(0);opacity:0}}
.femo{position:absolute;opacity:.55;animation:drift 7s ease-in-out infinite;z-index:2;filter:drop-shadow(0 0 8px currentColor)}
.femo svg{width:22px;height:22px;display:block}
@keyframes drift{0%,100%{transform:translateY(0) rotate(-5deg);opacity:.35}50%{transform:translateY(-18px) rotate(7deg);opacity:.9}}
.burst{position:absolute;left:50%;top:50%;width:10px;height:10px;border-radius:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:2;animation:bw .7s ease-out forwards}
@keyframes bw{from{box-shadow:0 0 0 0 rgba(255,255,255,.7),0 0 30px 10px rgba(56,189,248,.5);opacity:1}to{box-shadow:0 0 0 150px rgba(255,255,255,0),0 0 60px 30px rgba(139,92,246,0);opacity:0}}
@media(min-width:900px){.grid{grid-template-columns:repeat(2,1fr)}}'''

js = '''(function(){
var st=document.getElementById('stage');
var ICONS=['<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>','<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>','<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M12 2l2.4 7.6L22 12l-7.6 2.4L12 22l-2.4-7.6L2 12l7.6-2.4z"/></svg>','<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="7" y="7" width="10" height="10" rx="2"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2"/></svg>','<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>'];
var cols=['#38bdf8','#f43f5e','#8b5cf6','#2dd4bf','#fbbf24'];
if(st){
for(var j=0;j<6;j++){var f=document.createElement('span');f.className='femo';f.style.color=cols[j%cols.length];f.innerHTML=ICONS[j%ICONS.length];f.style.left=(5+Math.random()*88)+'%';f.style.top=(8+Math.random()*78)+'%';f.style.animationDelay=(Math.random()*5)+'s';st.appendChild(f)}
for(var i=0;i<16;i++){var s=document.createElement('i');s.className='spark';s.style.left=(Math.random()*96)+'%';s.style.top=(Math.random()*92)+'%';s.style.animationDelay=(Math.random()*4)+'s';s.style.animationDuration=(2.5+Math.random()*3)+'s';st.appendChild(s)}
}
var scenes=['sc1','sc2','sc3','sc4'];
var durs=[3000,5200,4600,3000];
var total=durs[0]+durs[1]+durs[2]+durs[3];
var idx=0,t0=Date.now(),s0=t0;
function type(el,txt){if(!el)return;el.textContent='';var i=0;el.classList.add('tw2');(function t(){i++;el.textContent=txt.slice(0,i);if(i<txt.length)setTimeout(t,60)})()}
var chatOn=false;
function startChat(){if(chatOn)return;chatOn=true;var box=document.getElementById('chatLoop');if(!box)return;var msgs=['Photoshop 2026 est disponible','Paiement M\\'Vola confirmé — lien envoyé','Besoin d\\'aide ? Agent disponible 24/7'];var mi=0;(function loop(){box.innerHTML='<span class="typing"><i></i><i></i><i></i></span>';setTimeout(function(){box.textContent=msgs[mi%msgs.length];mi++;setTimeout(loop,3200)},1000)})();}
function burst(){if(!st)return;var b=document.createElement('div');b.className='burst';st.appendChild(b);setTimeout(function(){b.remove()},750)}
function show(i){for(var k=0;k<scenes.length;k++){var e=document.getElementById(scenes[k]);if(e)e.classList.toggle('on',k===i)}
burst();
if(i===0)type(document.getElementById('tw1'),'Logiplus+');
if(i===1)startChat();
if(i===2){var f=document.querySelectorAll('.ifeat.pay');for(var j=0;j<f.length;j++){(function(el,d){setTimeout(function(){el.classList.add('on')},d)})(f[j],j*250)}}
if(i===3)type(document.getElementById('tw4'),'Prêt à commencer ?');}
setInterval(function(){var now=Date.now();if(now-s0>durs[idx]){s0=now;idx=(idx+1)%scenes.length;show(idx)}var el=(now-t0)%total},120);
show(0);
})();'''

c = open('index.html', encoding='utf-8').read()
old_sc2 = '<div class="iscene" id="sc2"><img class="iimg" src="img/hero.png" alt="Client et agent Logiplus+" onerror="this.style.display=\'none\'"><div class="chat-b client"><span class="who">Client</span>Bonjour ! Je cherche un logiciel de design 🎨</div><div class="chat-b agent" id="chatLoop"><span class="who">Agent Logiplus+</span>Bonjour ! Photoshop 2026 est disponible ✓</div></div>'
new_sc2 = '<div class="iscene" id="sc2"><div class="s2row"><img class="iimg" src="img/hero.png" alt="Client et agent Logiplus+" onerror="this.style.display=\'none\'"><div class="phone"><div class="ph-head">Agent Logiplus+ • en ligne</div><div class="ph-body"><div class="msg client">Bonjour ! Je cherche un logiciel de design</div><div class="msg agent" id="chatLoop">Bonjour ! Photoshop 2026 est disponible</div></div></div></div></div>'
c = c.replace(old_sc2, new_sc2)
c = c.replace('<div class="stage" id="stage">', '<div class="stage" id="stage"><i class="vig"></i>')
old_k = '<p class="stage-kicker">✨ Découvrez <span class="grad">vos logiciels préférés</span> sur notre plateforme ✨</p>'
new_k = '<p class="stage-kicker"><svg class="kstar" viewBox="0 0 24 24"><path d="M12 2l2.4 7.6L22 12l-7.6 2.4L12 22l-2.4-7.6L2 12l7.6-2.4z" fill="#fbbf24"/></svg> Découvrez <span class="grad">vos logiciels préférés</span> sur notre plateforme <svg class="kstar" viewBox="0 0 24 24"><path d="M12 2l2.4 7.6L22 12l-7.6 2.4L12 22l-2.4-7.6L2 12l7.6-2.4z" fill="#fbbf24"/></svg></p>'
c = c.replace(old_k, new_k)
open('hero.css','w',encoding='utf-8').write(css)
open('hero.js','w',encoding='utf-8').write(js)
open('index.html','w',encoding='utf-8').write(c)
print('OK - phone chat + svg neon + vignette + 2 colonnes')
