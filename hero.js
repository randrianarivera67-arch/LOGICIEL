(function(){
var el=document.getElementById('twText');
if(el){
var phrases=['Recherchez, cliquez, téléchargez — sans compte requis.','Paiement : Orange Money, M\'Vola, Airtel Money, PayPal.','Support client 24/7 — agent Logiplus+ à votre écoute.','Prix transparents fixés par l\'administrateur.'];
var pi=0,ci=phrases[0].length,del=true;
(function tick(){var p=phrases[pi];
if(del){ci--;if(ci<=0){ci=0;del=false;pi=(pi+1)%phrases.length;p=phrases[pi]}}
else{ci++;if(ci>=p.length){ci=p.length;el.textContent=p;del=true;setTimeout(tick,2200);return}}
el.textContent=p.slice(0,ci);setTimeout(tick,del?22:50)})();
}
var box=document.getElementById('chatLoop');
if(box){
var msgs=['Bonjour ! Photoshop 2026 est disponible ✓','Paiement M\'Vola confirmé — lien envoyé 🚀','Besoin d\'aide ? Agent disponible 24/7 💬'];
var mi=0;
(function loop(){box.innerHTML='<span class="who">Agent Logiplus+</span><span class="typing"><i></i><i></i><i></i></span>';
setTimeout(function(){box.innerHTML='<span class="who">Agent Logiplus+</span>'+msgs[mi%msgs.length];mi++;setTimeout(loop,3200)},1200)})();
}
})();
