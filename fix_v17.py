css = open('hero.css', encoding='utf-8').read()
css = css.replace('.ifeats{display:flex;gap:12px;flex-wrap:wrap;justify-content:center}', '.ifeats{display:grid;grid-template-columns:repeat(2,auto);gap:12px;justify-content:center}')
open('hero.css', 'w', encoding='utf-8').write(css)
print('OK - payment 2x2 toy ny modal')
