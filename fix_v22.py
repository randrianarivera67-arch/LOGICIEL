import re
css = open('hero.css', encoding='utf-8').read()
add = '''
.personwrap{position:relative;width:min(470px,92%);animation:floatDev 7s ease-in-out infinite;filter:drop-shadow(0 30px 60px rgba(0,0,0,.8))}
.personwrap img{width:100%;border-radius:20px;border:1px solid rgba(255,255,255,.15);display:block;animation:typingBob .5s ease-in-out infinite}
@keyframes typingBob{0%,100%{transform:translateY(0)}50%{transform:translateY(-2px)}}
.screen-glow{position:absolute;left:18%;top:16%;width:40%;height:34%;background:radial-gradient(ellipse at center,rgba(125,211,252,.28),transparent 70%);animation:flick 2.2s infinite;pointer-events:none}
@keyframes flick{0%,100%{opacity:.55}45%{opacity:.95}55%{opacity:.7}}
.tspark{position:absolute;width:5px;height:5px;border-radius:50%;background:#7dd3fc;box-shadow:0 0 8px 2px rgba(125,211,252,.6);animation:thand .45s infinite alternate}
.tspark.t1{left:38%;bottom:22%}
.tspark.t2{left:47%;bottom:20%;animation-delay:.15s;background:#f472b6;box-shadow:0 0 8px 2px rgba(244,114,182,.6)}
.tspark.t3{left:56%;bottom:22%;animation-delay:.3s}
@keyframes thand{from{transform:translateY(0);opacity:.9}to{transform:translateY(-4px);opacity:.4}}
'''
if '.personwrap{' not in css:
    css += add
    open('hero.css', 'w', encoding='utf-8').write(css)

c = open('index.html', encoding='utf-8').read()
m = re.search(r'<div class="devwrap">.*?</div></div></div>', c, flags=re.S)
if m:
    new = '<div class="personwrap"><img src="img/person.png" alt="Client utilisant un ordinateur" onerror="this.style.display=\'none\'"><i class="screen-glow"></i><span class="tspark t1"></span><span class="tspark t2"></span><span class="tspark t3"></span></div>'
    c = c.replace(m.group(0), new)
    open('index.html', 'w', encoding='utf-8').write(c)
    print('OK - olona mikitika ordinateur animé')
else:
    print('TADIO: devwrap tsy hita')
