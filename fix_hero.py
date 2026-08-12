c = open('index.html', encoding='utf-8').read()
if 'hero-vis' in c:
    print('Hero déjà animé - OK')
else:
    c = c.replace('<div class="hero">\n<span class="pill">', '<div class="hero"><div class="hero-grid"><div>\n<span class="pill">')
    c = c.replace("<p class=\"sub\">Recherchez, cliquez, téléchargez. Prix fixés par l'administrateur — aucune inscription requise.</p>", '<p class="sub"><span id="twText">Recherchez, cliquez, téléchargez — sans compte requis.</span><span class="tw-cursor"></span></p>')
    old = '<div><b id="statApp">0</b><span>Applications</span></div>\n</div>\n</div>'
    new = '''<div><b id="statApp">0</b><span>Applications</span></div>
</div>
<div class="hero-vis">
<img class="main" src="img/hero.png" alt="Client et agent Logiplus+" onerror="this.style.display='none'">
<div class="chat-b client"><span class="who">Client</span>Bonjour ! Je cherche un logiciel de design 🎨</div>
<div class="chat-b agent" id="chatLoop"><span class="who">Agent Logiplus+</span>Bonjour ! Photoshop 2026 est disponible ✓</div>
<span class="float-badge fb1">⚡ Téléchargement instantané</span>
<span class="float-badge fb2">🔒 Paiement sécurisé</span>
</div>
</div>
</div>'''
    c = c.replace(old, new)
    open('index.html', 'w', encoding='utf-8').write(c)
    print('OK - hero animé installé')
