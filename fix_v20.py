css = open('hero.css', encoding='utf-8').read()
css = css.replace('.ifeats{display:grid;grid-template-columns:repeat(2,auto);gap:12px;justify-content:center}', '.ifeats{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;justify-content:center;width:min(430px,92%)}')
css = css.replace('.devwrap{position:relative;width:min(250px,64%);', '.devwrap{position:relative;width:min(310px,84%);')
css = css.replace('.tab{position:relative;width:100%;aspect-ratio:3/4;', '.tab{position:relative;width:100%;aspect-ratio:4/3;')
css = css.replace('.mb{max-width:82%;padding:7px 10px;border-radius:16px;font-size:.6rem;', '.mb{max-width:82%;padding:6px 9px;border-radius:14px;font-size:.52rem;')
css = css.replace('.mhead b{font-size:.62rem;color:#fff;display:block}', '.mhead b{font-size:.56rem;color:#fff;display:block}')
css = css.replace('.mhead span{font-size:.5rem;color:#2dd4bf}', '.mhead span{font-size:.46rem;color:#2dd4bf}')
css = css.replace('.minput i{flex:1;font-style:normal;font-size:.55rem;color:#8a8f98}', '.minput i{flex:1;font-style:normal;font-size:.5rem;color:#8a8f98}')
if '.ifeats .ifeat.pay{width:100%}' not in css:
    css += '\n.ifeats .ifeat.pay{width:100%}\n'
open('hero.css', 'w', encoding='utf-8').write(css)
print('OK - panneaux mitovy + tablette landscape + chat kely')
