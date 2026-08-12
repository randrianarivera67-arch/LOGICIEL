css = open('hero.css', encoding='utf-8').read()
css = 'html,body{overflow-x:hidden;max-width:100%}\n' + css
css = css.replace('inset:-6%;background:url("img/stage-bg.png") center/cover no-repeat;animation:kb 26s ease-in-out infinite alternate;', 'inset:0;background:url("img/stage-bg.png") center/cover no-repeat;')
css = css.replace('font-size:clamp(.62rem,2.7vw,1.3rem);', 'font-size:clamp(.6rem,2.2vw,1.15rem);')
css += '\n#grid,.grid{grid-template-columns:1fr}\n@media(min-width:900px){#grid,.grid{grid-template-columns:repeat(2,1fr)}}\n'
open('hero.css', 'w', encoding='utf-8').write(css)
print('OK - tsy misy zoom + tsy deborde + 2 colonnes PC')
