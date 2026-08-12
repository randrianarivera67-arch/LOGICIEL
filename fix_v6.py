css = open('hero.css', encoding='utf-8').read()
if 'overflow-x:hidden!important' not in css:
    css = 'html,body{overflow-x:hidden!important;max-width:100%!important}\n#view-home,.container,.hero{max-width:100%;overflow-x:clip}\n' + css
css = css.replace('max-width:860px;margin:0 auto 26px', 'max-width:min(860px,100%);margin:0 auto 26px')
css = css.replace('.stage{position:relative;max-width:min(860px,100%);', '.stage{position:relative;width:100%;max-width:min(820px,100%);')
open('hero.css', 'w', encoding='utf-8').write(css)
print('OK v6 - containment total')
