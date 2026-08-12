import re

c = open('index.html', encoding='utf-8').read()
c = c.replace('>View All<', '>Voir tout<')

# 1. Esorina ny bordure teal amin'ny panneau listTitle
def fix_div(m):
    tag = m.group(0)
    if 'style=' not in tag:
        tag = tag.replace('>', ' style="border-left:none!important">', 1)
    return tag
c = re.sub(r'<div class="[^"]+"[^>]*>(?=\s*<h2 id="listTitle")', fix_div, c, count=1)

# 2. Bouton Voir tout = bleu ciel
c = re.sub(r'<button([^>]*>Voir tout</button>)', '<button style="background:linear-gradient(135deg,#38bdf8,#0ea5e9);color:#fff;border-color:transparent;font-weight:700"\\1', c, count=1)
open('index.html', 'w', encoding='utf-8').write(c)

# 3. Malagasy -> Français ao amin'ny pay.js
p = open('pay.js', encoding='utf-8').read()
p = p.replace('Safidio ny fomba fandoavana :', 'Choisissez le moyen de paiement :')
p = p.replace('Votre numéro (nandefasana)', 'Votre numéro (envoyé depuis)')
p = p.replace('💡 Alefaso ao amin\'ny dossier <b>data/</b> ny settings.json voadika mba ho hitan\'ny client ny numéro.', '💡 Placez le fichier <b>settings.json</b> exporté dans le dossier <b>data/</b> pour que les clients voient vos numéros.')
open('pay.js', 'w', encoding='utf-8').write(p)
print('OK - bordure esorina + Voir tout bleu ciel + français partout')
