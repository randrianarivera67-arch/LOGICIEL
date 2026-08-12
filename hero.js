(function(){
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
function startChat(){if(chatOn)return;chatOn=true;var box=document.getElementById('chatLoop');if(!box)return;var msgs=['Photoshop 2026 est disponible','Paiement M\'Vola confirmé — lien envoyé','Besoin d\'aide ? Agent disponible 24/7'];var mi=0;(function loop(){box.innerHTML='<span class="typing"><i></i><i></i><i></i></span>';setTimeout(function(){box.textContent=msgs[mi%msgs.length];mi++;setTimeout(loop,3200)},1000)})();}
function burst(){if(!st)return;var b=document.createElement('div');b.className='burst';st.appendChild(b);setTimeout(function(){b.remove()},750)}
function show(i){for(var k=0;k<scenes.length;k++){var e=document.getElementById(scenes[k]);if(e)e.classList.toggle('on',k===i)}
burst();
if(i===0)type(document.getElementById('tw1'),'Logiplus+');
if(i===1)startChat();
if(i===2){var f=document.querySelectorAll('.ifeat.pay');for(var j=0;j<f.length;j++){(function(el,d){setTimeout(function(){el.classList.add('on')},d)})(f[j],j*250)}}
if(i===3)type(document.getElementById('tw4'),'Prêt à commencer ?');}
setInterval(function(){var now=Date.now();if(now-s0>durs[idx]){s0=now;idx=(idx+1)%scenes.length;show(idx)}var el=(now-t0)%total},120);
show(0);
})();