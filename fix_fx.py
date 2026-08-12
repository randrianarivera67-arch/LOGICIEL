css = '''.stage{position:relative;max-width:860px;margin:0 auto 26px;height:360px;border-radius:24px;border:1px solid var(--border);overflow:hidden;backdrop-filter:blur(10px);background:linear-gradient(120deg,rgba(56,189,248,.18),rgba(244,63,94,.15),rgba(139,92,246,.2),rgba(56,189,248,.18));background-size:300% 300%;animation:gradMove 12s ease infinite}
@keyframes gradMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
@media(max-width:640px){.stage{height:340px}}
.sbar{position:absolute;left:0;bottom:0;height:3px;width:100%;background:rgba(255,255,255,.08);z-index:4}
.sbar i{display:block;height:100%;width:0;background:var(--grad)}
.iscene{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:20px;opacity:0;transform:scale(.97);transition:opacity .7s,transform .7s;text-align:center;z-index:3}
.iscene.on{opacity:1;transform:scale(1)}
.iscene h2{font-family:Sora,sans-serif;font-size:clamp(1.4rem,4vw,2.4rem);font-weight:800;text-shadow:0 4px 24px rgba(0,0,0,.45)}
.iscene p{color:var(--soft2);font-size:.92rem;max-width:520px}
.ilogo{width:64px;height:64px;filter:drop-shadow(0 0 18px rgba(56,189,248,.7))}
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
@keyframes blink{50%{opacity:0}}
.spark{position:absolute;width:6px;height:6px;border-radius:50%;background:#fff;opacity:0;animation:spop linear infinite;z-index:1;box-shadow:0 0 8px 2px rgba(255,255,255,.5)}
.spark:nth-child(3n){background:#38bdf8;box-shadow:0 0 10px 3px rgba(56,189,248,.6)}
.spark:nth-child(3n+1){background:#f43f5e;box-shadow:0 0 10px 3px rgba(244,63,94,.6)}
.spark:nth-child(3n+2){background:#8b5cf6;box-shadow:0 0 10px 3px rgba(139,92,246,.6)}
@keyframes spop{0%{transform:scale(0);opacity:0}20%{opacity:1}50%{transform:scale(1.5);opacity:.9}100%{transform:scale(0);opacity:0}}
.femo{position:absolute;font-size:1.15rem;opacity:.4;animation:drift 7s ease-in-out infinite;z-index:1;filter:drop-shadow(0 0 6px rgba(56,189,248,.6))}
@keyframes drift{0%,100%{transform:translateY(0) rotate(-5deg);opacity:.3}50%{transform:translateY(-18px) rotate(7deg);opacity:.85}}
.burst{position:absolute;left:50%;top:50%;width:10px;height:10px;border-radius:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:2;animation:bw .7s ease-out forwards}
@keyframes bw{from{box-shadow:0 0 0 0 rgba(255,255,255,.7),0 0 30px 10px rgba(56,189,248,.5);opacity:1}to{box-shadow:0 0 0 150px rgba(255,255,255,0),0 0 60px 30px rgba(139,92,246,0);opacity:0}}'''

js = '''(function(){
var st=document.getElementById('stage');
if(st){
var em=['💻','','✨','','🖱️','💾'];
for(var j=0;j<6;j++){var f=document.createElement('span');f.className='femo';f.textContent=em[j%em.length];f.style.left=(5+Math.random()*88)+'%';f.style.top=(8+Math.random()*78)+'%';f.style.animationDelay=(Math.random()*5)+'s';st.appendChild(f)}
for(var i=0;i<16;i++){var s=document.createElement('i');s.className='spark';s.style.left=(Math.random()*96)+'%';s.style.top=(Math.random()*92)+'%';s.style.animationDelay=(Math.random()*4)+'s';s.style.animationDuration=(2.5+Math.random()*3)+'s';st.appendChild(s)}
}
var scenes=['sc1','sc2','sc3','sc4'];
var durs=[3000,4600,4600,3000];
var total=durs[0]+durs[1]+durs[2]+durs[3];
var idx=0,t0=Date.now(),s0=t0;
function type(el,txt){if(!el)return;el.textContent='';var i=0;el.classList.add('tw2');(function t(){i++;el.textContent=txt.slice(0,i);if(i<txt.length)setTimeout(t,60)})()}
var chatOn=false;
function startChat(){if(chatOn)return;chatOn=true;var box=document.getElementById('chatLoop');if(!box)return;var msgs=['Bonjour ! Photoshop 2026 est disponible ✓','Paiement M\\'Vola confirmé — lien envoyé 🚀','Besoin d\\'aide ? Agent disponible 24/7 💬'];var mi=0;(function loop(){box.innerHTML='<span class="who">Agent Logiplus+</span><span class="typing"><i></i><i></i><i></i></span>';setTimeout(function(){box.innerHTML='<span class="who">Agent Logiplus+</span>'+msgs[mi%msgs.length];mi++;setTimeout(loop,3200)},1000)})();}
function burst(){if(!st)return;var b=document.createElement('div');b.className='burst';st.appendChild(b);setTimeout(function(){b.remove()},750)}
function show(i){for(var k=0;k<scenes.length;k++){var e=document.getElementById(scenes[k]);if(e)e.classList.toggle('on',k===i)}
burst();
if(i===0)type(document.getElementById('tw1'),'Logiplus+');
if(i===1)startChat();
if(i===2){var f=document.querySelectorAll('.ifeat.pay');for(var j=0;j<f.length;j++){(function(el,d){setTimeout(function(){el.classList.add('on')},d)})(f[j],j*250)}}
if(i===3)type(document.getElementById('tw4'),'Prêt à commencer ?');}
setInterval(function(){var now=Date.now();if(now-s0>durs[idx]){s0=now;idx=(idx+1)%scenes.length;show(idx)}var el=(now-t0)%total;var b=document.getElementById('stageBar');if(b)b.style.width=(el/total*100)+'%'},120);
show(0);
})();'''

open('hero.css','w',encoding='utf-8').write(css)
open('hero.js','w',encoding='utf-8').write(js)
print('OK - fx animé ajouté')
