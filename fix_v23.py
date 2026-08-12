import re

css = open('hero.css', encoding='utf-8').read()
add = '''
.osrow{display:flex;gap:20px;align-items:stretch;justify-content:center;flex-wrap:wrap}
.osic{display:flex;flex-direction:column;align-items:center;gap:6px;padding:16px 18px;border-radius:20px;border:1px solid rgba(255,255,255,.15);background:rgba(5,8,15,.72);opacity:0;transform:translateY(26px) scale(.7);transition:.6s cubic-bezier(.2,.9,.3,1.35)}
.osic.on{opacity:1;transform:translateY(0) scale(1)}
.osic svg{width:44px;height:44px;filter:drop-shadow(0 0 10px currentColor)}
.osic span{font-size:.62rem;color:#dbe6f5;font-weight:700}
'''
if '.osrow{' not in css:
    css += add
    open('hero.css', 'w', encoding='utf-8').write(css)

js = open('hero.js', encoding='utf-8').read()
js = js.replace("if(i===1)startChat();", "if(i===1){startChat();var o=document.querySelectorAll('.osic');for(var k2=0;k2<o.length;k2++){(function(el,d){setTimeout(function(){el.classList.add('on')},d)})(o[k2],200+k2*300)}}")
if "se.addEventListener('keydown'" not in js:
    js += '''
(function(){var se=document.getElementById('search');if(se){se.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();se.blur();var g=document.getElementById('grid');if(g)g.scrollIntoView({behavior:'smooth',block:'start'})}})}})();'''
    open('hero.js', 'w', encoding='utf-8').write(js)

c = open('index.html', encoding='utf-8').read()
m = re.search(r'<div class="personwrap">.*?</span></div>', c, flags=re.S)
if m:
    new = '<div class="osrow"><div class="osic" style="color:#38bdf8"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 5l8-1.2V11H3zM13 3.6L21 2.5V11h-8zM3 13h8v7.2L3 19zM13 13h8v8.5l-8-1.1z"/></svg><span>Windows</span></div><div class="osic" style="color:#e8ecf8"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M16.7 12.9c0-2 1.6-3 1.7-3.1-1-1.4-2.4-1.6-2.9-1.6-1.2-.1-2.4.7-3 .7-.6 0-1.6-.7-2.6-.7-1.3 0-2.6.8-3.3 2-1.4 2.4-.4 6 1 8 .7 1 1.5 2.1 2.6 2 1-.1 1.4-.7 2.6-.7s1.6.7 2.6.7c1.1 0 1.8-1 2.5-2 .8-1.1 1.1-2.2 1.1-2.3-.1 0-2.2-.9-2.3-3z"/><path d="M14.8 6.2c.5-.7.9-1.6.8-2.6-.8 0-1.8.6-2.3 1.3-.5.6-1 1.6-.8 2.5.9.1 1.8-.5 2.3-1.2z"/></svg><span>macOS</span></div><div class="osic" style="color:#3ddc84"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 16a8 8 0 0 1 16 0z"/><path d="M7 8L5.5 5.5M17 8l1.5-2.5"/><circle cx="9.5" cy="12.5" r=".6" fill="currentColor"/><circle cx="14.5" cy="12.5" r=".6" fill="currentColor"/></svg><span>Android</span></div><div class="osic" style="color:#fbbf24"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 3c-2 0-3.2 1.5-3.2 3.5 0 1.4-.4 2.5-1.1 3.6-.8 1.3-1.4 2.8-1.4 4.4 0 3 2.5 5.5 5.7 5.5s5.7-2.5 5.7-5.5c0-1.6-.6-3.1-1.4-4.4-.7-1.1-1.1-2.2-1.1-3.6C15.2 4.5 14 3 12 3z"/><path d="M9.5 13c.5 2 1.4 3 2.5 3s2-1 2.5-3"/><circle cx="10.8" cy="6.5" r=".5" fill="currentColor"/><circle cx="13.2" cy="6.5" r=".5" fill="currentColor"/></svg><span>Linux</span></div></div>'
    c = c.replace(m.group(0), new)
    open('index.html', 'w', encoding='utf-8').write(c)
    print('OK - 4 OS icons + Enter search fix')
else:
    print('TADIO: personwrap tsy hita')
