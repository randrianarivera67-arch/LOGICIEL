css = open('hero.css', encoding='utf-8').read()
old = 'border:1px solid var(--border);overflow:hidden;background:#05070f}'
new = 'border:1.5px solid rgba(251,191,36,.65);overflow:hidden;background:#05070f;box-shadow:0 0 0 1px rgba(251,191,36,.22),0 0 34px rgba(251,191,36,.3),0 18px 70px -25px rgba(0,0,0,.85);animation:goldPulse 3.5s ease-in-out infinite}'
css = css.replace(old, new, 1)
if '@keyframes goldPulse' not in css:
    css += '''
@keyframes goldPulse{0%,100%{box-shadow:0 0 0 1px rgba(251,191,36,.22),0 0 22px rgba(251,191,36,.22),0 18px 70px -25px rgba(0,0,0,.85);border-color:rgba(251,191,36,.5)}50%{box-shadow:0 0 0 1px rgba(251,191,36,.5),0 0 46px rgba(251,191,36,.5),0 18px 70px -25px rgba(0,0,0,.85);border-color:rgba(251,191,36,.95)}}'''
open('hero.css', 'w', encoding='utf-8').write(css)
print('OK - bordure doree mamirapiratra')
