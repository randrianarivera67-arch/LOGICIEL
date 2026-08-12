with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Soloina ny brand span: Logiplus → Logiplus<sup>+</sup>
content = content.replace(
    '<span>Logiplus</span>',
    '<span>Logiplus<sup style="font-size:0.6em;vertical-align:super;color:var(--amber)">+</sup></span>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK - superscript ajouté')
