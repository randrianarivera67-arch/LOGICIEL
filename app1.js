var ADMIN_PASS='admin123';
var DB_KEY='logiciel_db_v3';
console.log('Logiciel v11 loaded');
function storeGet(k){try{return localStorage.getItem(k)}catch(e){return null}}
function storeSet(k,v){try{localStorage.setItem(k,v)}catch(e){}}
function storeDel(k){try{localStorage.removeItem(k)}catch(e){}}
function sessGet(k){try{return sessionStorage.getItem(k)}catch(e){return null}}
function sessSet(k,v){try{sessionStorage.setItem(k,v)}catch(e){}}
function sessDel(k){try{sessionStorage.removeItem(k)}catch(e){}}
function gid(id){return document.getElementById(id)}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function hashN(s){var a=0,t=String(s||'');for(var i=0;i<t.length;i++){a+=t.charCodeAt(i)}return a}
function initials(n){var w=String(n||'').trim().split(/\s+/).slice(0,2);return w.map(function(x){return x.charAt(0)}).join('').toUpperCase()}
function toast(msg){var t=document.createElement('div');t.className='toast';t.textContent=msg;gid('toasts').appendChild(t);setTimeout(function(){t.style.opacity='0';t.style.transition='.4s';setTimeout(function(){t.remove()},400)},2800)}
function bind(id,ev,fn){var el=gid(id);if(el){el.addEventListener(ev,fn)}}
window.addEventListener('error',function(e){if(e.message){toast('⚠️ Erreur : '+e.message)}});
function applyThemeIcon(){var l=document.body.classList.contains('light');gid('themeUse').setAttribute('href',l?'#i-moon':'#i-sun')}
function toggleTheme(){var l=document.body.classList.toggle('light');storeSet('lg_theme',l?'light':'dark');applyThemeIcon();toast(l?'Mode clair ☀️':'Mode sombre 🌙')}
var SEEDS=[
{id:'s1',name:'Adobe Photoshop 2026',type:'Logiciel',category:'Design',os:'Windows',version:'27.0',size:'4.8 Go',dl:174205,rate:4.5,price:'120 000 Ar',image:'',link:'https://www.adobe.com/fr/products/photoshop.html',date:'2026-08-05',info:"Retouche photo et design graphique avec IA Firefly.",install:"Téléchargez\nExécutez Setup.exe\nSuivez l'assistant\nSaisissez votre licence\nLancez Photoshop ✓"},
{id:'s2',name:'Adobe Premiere Pro 2026',type:'Logiciel',category:'Vidéo',os:'Windows',version:'26.2',size:'6.1 Go',dl:98230,rate:4.5,price:'120 000 Ar',image:'',link:'https://www.adobe.com/fr/products/premiere.html',date:'2026-08-04',info:"Montage vidéo pro : étalonnage, multicam, sous-titres IA.",install:"Téléchargez\nLancez l'installation\nChoisissez la langue\nActivez votre licence\nMontez votre projet 🎬"},
{id:'s3',name:'Microsoft Office 2026',type:'Logiciel',category:'Bureautique',os:'Windows',version:'16.111',size:'3.9 Go',dl:283889,rate:4,price:'80 000 Ar',image:'',link:'https://www.microsoft.com/microsoft-365',date:'2026-08-03',info:"Suite bureautique : Word, Excel, PowerPoint, Outlook, Copilot.",install:"Téléchargez\nExécutez et connectez-vous\nSélectionnez les apps\nAttendez le téléchargement\nOuvrez Word et activez"},
{id:'s4',name:'Windows 11 Pro',type:'Logiciel',category:'Système',os:'Windows',version:'26H2',size:'5.4 Go',dl:452100,rate:4.5,price:'60 000 Ar',image:'',link:'https://www.microsoft.com/windows/windows-11',date:'2026-08-01',info:"Nouveau menu, Snap Layouts, sécurité renforcée.",install:"Téléchargez l'ISO\nCréez une clé USB bootable\nDémarrez sur la clé\nChoisissez Installer\nConfigurez votre session"},
{id:'s5',name:'YouTube Vanced',type:'Application',category:'Divertissement',os:'Android',version:'21.31',size:'125 Mo',dl:294413,rate:4,price:'20 000 Ar',image:'',link:'https://vanced.app',date:'2026-07-30',info:"Block all ads. Lecture en arrière-plan incluse.",install:"Téléchargez APK\nAutorisez sources inconnues\nInstallez\nConnectez-vous\nProfitez Pro ✓"},
{id:'s6',name:'Canva Pro',type:'Application',category:'Design',os:'Android',version:'2026.8',size:'150 Mo',dl:187300,rate:4,price:'30 000 Ar',image:'',link:'https://www.canva.com',date:'2026-07-27',info:"Visuels pro : modèles, suppression fond, kit marque.",install:"Téléchargez\nInstallez et lancez\nConnectez-vous\nPro activé\nCréez votre design 🎨"},
{id:'s7',name:'Kaspersky Premium',type:'Logiciel',category:'Sécurité',os:'Windows',version:'2026',size:'850 Mo',dl:121951,rate:4.5,price:'45 000 Ar',image:'',link:'https://www.kaspersky.com',date:'2026-07-25',info:"Antivirus temps réel, VPN, protection bancaire.",install:"Téléchargez\nLancez (fermez autres antivirus)\nAcceptez la licence\nActivez\nLancez première analyse 🛡️"},
{id:'s8',name:'Internet Download Manager',type:'Logiciel',category:'Download Managers',os:'Windows',version:'6.42',size:'12 Mo',dl:435790,rate:4.5,price:'25 000 Ar',image:'',link:'https://www.internetdownloadmanager.com',date:'2026-07-22',info:"Accélérateur jusqu'à 5x, reprise téléchargements.",install:"Téléchargez\nExécutez idman.exe\nSuivez l'assistant\nRedémarrez navigateur\nProfitez intégration ✓"},
{id:'s9',name:'Altium Designer',type:'Logiciel',category:'Engineering',os:'Windows',version:'26.9',size:'3.15 Go',dl:165918,rate:4,price:'150 000 Ar',image:'',link:'https://www.altium.com',date:'2026-07-20',info:"PCB Design 2D/3D, collaboration cloud.",install:"Téléchargez\nExécutez en admin\nChoisissez langue\nSaisissez licence\nConfigurez gabarits"},
{id:'s10',name:'WinRAR',type:'Logiciel',category:'Tools & Utilities',os:'Windows',version:'7.10',size:'3.5 Mo',dl:512340,rate:4.5,price:'15 000 Ar',image:'',link:'https://www.rarlab.com',date:'2026-07-15',info:"Compresseur RAR/ZIP/7z, chiffrement AES-256.",install:"Téléchargez\nExécutez winrar.exe\nCliquez Installer\nAssociez formats\nClic droit pour extraire ✓"}];
var state={list:[],query:'',cat:'Tous',type:'Tous',editingId:null,authed:sessGet('lg_admin')==='1'};
function loadDB(done){
var local=null;
try{local=JSON.parse(storeGet(DB_KEY))}catch(e){}
if(local&&local.length){state.list=local;done();return}
fetch('data/logiciels.json',{cache:'no-store'})
.then(function(r){return r.ok?r.json():null})
.then(function(j){state.list=(j&&j.length)?j:SEEDS;done()})
.catch(function(){state.list=SEEDS;done()})
}
function saveDB(){storeSet(DB_KEY,JSON.stringify(state.list))}
function closeMenu(){gid('mobileMenu').hidden=true;gid('burgerUse').setAttribute('href','#i-menu')}
function toggleMenu(){var m=gid('mobileMenu');m.hidden=!m.hidden;gid('burgerUse').setAttribute('href',m.hidden?'#i-menu':'#i-close')}
function goHome(e){if(e)e.preventDefault();closeMenu();if(location.hash&&location.hash!=='#/'){location.hash='#/'}router()}
function goAdmin(e){if(e)e.preventDefault();closeMenu();if(location.hash!=='#/admin'){location.hash='#/admin'}router()}
function pickCat(c){state.cat=c;closeMenu();if(location.hash&&location.hash!=='#/'){location.hash='#/'}router()}
function viewAll(){state.cat='Tous';state.type='Tous';state.query='';gid('search').value='';renderSeg();renderCats();renderGrid()}
function togglePass(){gid('loginPass').type=gid('showPass').checked?'text':'password'}
function doLogin(){var v=(gid('loginPass').value||'').trim();if(!v){toast('Saisissez le mot de passe');return false}
if(v===ADMIN_PASS){state.authed=true;sessSet('lg_admin','1');renderAdmin();toast('Bienvenue admin 👋')}else{toast('Mot de passe incorrect ❌')}
gid('loginPass').value='';return false}
function coverHTML(it){if(it.image)return '<img src="'+esc(it.image)+'" alt="" loading="lazy">';return '<div class="cover-fb cg'+(hashN(it.name)%5)+'"><span>'+esc(initials(it.name))+'</span></div>'}
function osInfo(os){var o=String(os||'').toLowerCase();if(o.indexOf('win')===0)return{ic:'#i-windows',c:'#38bdf8'};if(o.indexOf('mac')===0||o.indexOf('ios')===0)return{ic:'#i-apple',c:'#64748b'};if(o.indexOf('and')===0)return{ic:'#i-android',c:'#22c55e'};return{ic:'#i-monitor',c:'#93a0b8'}}
function starsHTML(r){var rate=parseFloat(r);if(isNaN(rate))rate=4.5;var out='';for(var i=1;i<=5;i++){var cls=rate>=i?'st-full':(rate>i-1?'st-half':'st-empty');out+='<svg class="star '+cls+'" viewBox="0 0 24 24"><use href="#i-star"></use></svg>'}return out}
function fmtSize(sz){var m=String(sz||'').match(/([\d.,]+)\s*([A-Za-z]+)?/);if(m)return '<b>'+esc(m[1])+'</b>'+(m[2]?'<i>'+esc(m[2])+'</i>':'');return '<b>'+esc(sz||'—')+'</b>'}
function filtered(){var q=state.query.toLowerCase();return state.list.filter(function(it){var type=it.type||'Logiciel';var cat=it.category||'Autre';if(state.type!=='Tous'&&type!==state.type)return false;if(state.cat!=='Tous'&&cat!==state.cat)return false;if(q&&it.name.toLowerCase().indexOf(q)===-1&&cat.toLowerCase().indexOf(q)===-1)return false;return true}).sort(function(a,b){return String(b.date||'').localeCompare(String(a.date||''))})}
function renderStats(){gid('statCount').textContent=state.list.length;gid('statLog').textContent=state.list.filter(function(i){return(i.type||'Logiciel')==='Logiciel'}).length;gid('statApp').textContent=state.list.filter(function(i){return i.type==='Application'}).length}
function renderSeg(){var btns=gid('segType').querySelectorAll('button');for(var i=0;i<btns.length;i++){btns[i].classList.toggle('active',btns[i].getAttribute('data-type')===state.type)}}
function renderCats(){var seen={},cats=['Tous'];state.list.forEach(function(i){var c=i.category||'Autre';if(!seen[c]){seen[c]=1;cats.push(c)}});var html=cats.map(function(c){return '<a href="#/" class="cat-link'+(c===state.cat?' active':'')+'" data-cat="'+esc(c)+'">'+esc(c)+'</a>'}).join('');gid('catsNav').innerHTML=html;gid('mmCats').innerHTML=html}
function renderGrid(){var items=filtered();renderStats();gid('resultInfo').textContent=items.length+' résultat'+(items.length>1?'s':'');gid('empty').hidden=items.length>0;var title=state.cat!=='Tous'?state.cat:(state.type==='Tous'?'Tous les produits':(state.type==='Logiciel'?'Windows & Logiciels':'Applications'));gid('listTitle').textContent=title;gid('grid').innerHTML=items.map(function(it,i){var type=it.type||'Logiciel';var os=osInfo(it.os);return '<article class="card" data-open="'+esc(it.id)+'" style="animation-delay:'+(i*40)+'ms"><div class="c-top"><div class="c-icon"><span class="t-badge tb-'+esc(type)+'">'+esc(type)+'</span>'+coverHTML(it)+'<span class="p-badge">'+esc(it.price||'—')+'</span></div><div class="c-head"><h3>'+esc(it.name)+(it.version?' '+esc(it.version):'')+'</h3><p class="c-desc">'+esc(it.info||'')+'</p><span class="c-cat">'+esc(it.category||'Autre')+'</span></div></div><div class="c-mid"><span class="c-os"><svg class="ni ni-sm" style="color:'+os.c+';filter:none"><use href="'+os.ic+'"></use></svg>'+esc(it.os||'Autre')+'</span><span class="c-dl"><svg class="ni ni-sm" style="color:var(--muted);filter:none"><use href="#i-cloud-dl"></use></svg>'+esc(it.dl||0)+'</span></div><div class="c-bot"><div class="c-rep"><span>Reputation</span><div class="stars">'+starsHTML(it.rate)+'</div></div><div class="c-size">'+fmtSize(it.size)+'</div></div></article>'}).join('')}
