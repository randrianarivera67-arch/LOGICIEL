(function(){
var scenes=['sc1','sc2','sc3','sc4'];
var durs=[3000,4600,4600,3000];
var total=durs[0]+durs[1]+durs[2]+durs[3];
var idx=0,t0=Date.now(),s0=t0;
function type(el,txt){if(!el)return;el.textContent='';var i=0;el.classList.add('tw2');(function t(){i++;el.textContent=txt.slice(0,i);if(i<txt.length)setTimeout(t,60)})()}
var chatOn=false;
function startChat(){if(chatOn)return;chatOn=true;var box=document.getElementById('chatLoop');if(!box)return;var msgs=['Bonjour ! Photoshop 2026 est disponible ✓','Paiement M\'Vola confirmé — lien envoyé 🚀','Besoin d\'aide ? Agent disponible 24/7 💬'];var mi=0;(function loop(){box.innerHTML='<span class="who">Agent Logiplus+</span><span class="typing"><i></i><i></i><i></i></span>';setTimeout(function(){box.innerHTML='<span class="who">Agent Logiplus+</span>'+msgs[mi%msgs.length];mi++;setTimeout(loop,3200)},1000)})();}
function show(i){for(var k=0;k<scenes.length;k++){var e=document.getElementById(scenes[k]);if(e)e.classList.toggle('on',k===i)}
if(i===0)type(document.getElementById('tw1'),'Logiplus+');
if(i===1)startChat();
if(i===2){var f=document.querySelectorAll('.ifeat.pay');for(var j=0;j<f.length;j++){(function(el,d){setTimeout(function(){el.classList.add('on')},d)})(f[j],j*250)}}
if(i===3)type(document.getElementById('tw4'),'Prêt à commencer ?');}
setInterval(function(){var now=Date.now();if(now-s0>durs[idx]){s0=now;idx=(idx+1)%scenes.length;show(idx)}var el=(now-t0)%total;var b=document.getElementById('stageBar');if(b)b.style.width=(el/total*100)+'%'},120);
show(0);
})();