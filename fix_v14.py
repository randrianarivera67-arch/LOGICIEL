import json

js = r'''{id:'s11',name:'FL Studio 2026',type:'Logiciel',category:'DAW',os:'Windows',version:'2026.1',size:'1.2 Go',dl:388210,rate:4.5,price:'70 000 Ar',image:'',link:'https://www.image-line.com',date:'2026-08-10',info:"DAW complet : composition, mixage, mastering, lifetime updates.",install:"Téléchargez\nExécutez l'installateur\nChoisissez les composants\nLancez FL Studio\nActivez votre licence"},
{id:'s12',name:'Ableton Live 12 Suite',type:'Logiciel',category:'DAW',os:'Windows',version:'12.1',size:'4.2 Go',dl:145900,rate:5,price:'90 000 Ar',image:'',link:'https://www.ableton.com',date:'2026-08-09',info:"DAW référence pour scène et production électronique.",install:"Téléchargez\nExécutez le setup\nConnectez votre compte\nLancez Live\nActivez la licence"},
{id:'s13',name:'Logic Pro 11',type:'Logiciel',category:'DAW',os:'macOS',version:'11.0',size:'1.8 Go',dl:98770,rate:4.5,price:'80 000 Ar',image:'',link:'https://www.apple.com/logic-pro/',date:'2026-08-08',info:"DAW pro Apple : spatial audio, sessions live.",install:"Téléchargez\nInstallez via App Store\nOuvrez Logic Pro\nValidez la licence\nCréez votre projet"},
{id:'s14',name:'Xfer Serum 2',type:'Logiciel',category:'VST Plugins',os:'Windows',version:'2.0',size:'320 Mo',dl:210450,rate:5,price:'40 000 Ar',image:'',link:'https://xferrecords.com',date:'2026-08-07',info:"Synthé wavetable puissant, standard de la prod moderne.",install:"Téléchargez\nExécutez l'installeur\nChoisissez VST3/AU\nScannez les plugins dans votre DAW\nProfitez"},
{id:'s15',name:'Omnisphere 4',type:'Logiciel',category:'VST Plugins',os:'Windows',version:'4.0',size:'8.6 Go',dl:87600,rate:4.5,price:'110 000 Ar',image:'',link:'https://www.spectrasonics.net',date:'2026-08-06',info:"Bibliothèque sonore immense : 20 000+ presets.",install:"Téléchargez\nInstallez + registre\nEntrez le serial\nScannez dans votre DAW\nExplorez les presets"},
{id:'s16',name:'Kontakt 8',type:'Logiciel',category:'VST Plugins',os:'Windows',version:'8.2',size:'1.4 Go',dl:165400,rate:4.5,price:'60 000 Ar',image:'',link:'https://www.native-instruments.com',date:'2026-08-05',info:"Lecteur d'instruments virtuels n°1 (pianos, cordes, drums).",install:"Téléchargez\nInstallez Kontakt\nAjoutez les librairies\nScannez dans votre DAW\nJouez"}'''

a = open('app1.js', encoding='utf-8').read()
if 'FL Studio' not in a:
    marker = 'Clic droit pour extraire ✓"}];'
    a = a.replace(marker, 'Clic droit pour extraire ✓"},\n' + js + '];')
    open('app1.js', 'w', encoding='utf-8').write(a)
    print('OK - SEEDS +6 (DAW & VST Plugins)')
else:
    print('SEEDS efa misy DAW/VST')

try:
    d = json.load(open('data/logiciels.json', encoding='utf-8'))
except Exception:
    d = []
if not any(i.get('id') == 's11' for i in d):
    d.extend(json.loads('[' + js.replace(r"\n", r"\\n") + ']'))
    json.dump(d, open('data/logiciels.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('OK - logiciels.json +6')
else:
    print('JSON efa misy DAW/VST')
