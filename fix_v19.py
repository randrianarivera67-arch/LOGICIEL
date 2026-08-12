css = open('hero.css', encoding='utf-8').read()
css = css.replace('.ifeat.pay img{width:44px;height:44px;border-radius:10px;object-fit:cover}', '.ifeat.pay .lgw{margin:0 auto}')
add = '''
.lgw{width:52px;height:52px;border-radius:12px;overflow:hidden;display:block;background:#0b0f14}
.lgw img{width:100%;height:100%;object-fit:cover;border-radius:12px;display:block}
.lgw.z1 img{transform:scale(1.35)}
.lgw.z2 img{transform:scale(1.5)}
.devwrap{position:relative;width:min(250px,64%);animation:floatDev 6s ease-in-out infinite;filter:drop-shadow(0 34px 60px rgba(0,0,0,.8))}
@keyframes floatDev{0%,100%{transform:translateY(0) rotate(-1.5deg)}50%{transform:translateY(-14px) rotate(1.5deg)}}
.tab{position:relative;width:100%;aspect-ratio:3/4;border-radius:26px;background:linear-gradient(145deg,#8a8f98,#3d4148 30%,#17191d 70%,#0a0b0d);padding:10px;box-shadow:inset 0 0 4px rgba(255,255,255,.35),0 0 0 1px rgba(255,255,255,.12),0 0 34px rgba(56,189,248,.22)}
.tab .cam{position:absolute;top:5px;left:50%;transform:translateX(-50%);width:6px;height:6px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#4a5568,#000 70%);z-index:6}
.tab .scr{position:relative;width:100%;height:100%;border-radius:17px;background:#0d1117;overflow:hidden;display:flex;flex-direction:column}
.tab .scr::after{content:'';position:absolute;inset:0;background:linear-gradient(115deg,transparent 40%,rgba(255,255,255,.06) 45%,rgba(255,255,255,.12) 50%,transparent 55%);pointer-events:none;z-index:7}
.tab .hb{position:absolute;bottom:4px;left:50%;transform:translateX(-50%);width:64px;height:4px;border-radius:99px;background:rgba(255,255,255,.4);z-index:8}
.mhead{display:flex;align-items:center;gap:8px;padding:14px 10px 8px;background:rgba(13,17,23,.95)}
.mava{width:26px;height:26px;border-radius:50%;background:linear-gradient(135deg,#00c6ff,#0078ff);display:grid;place-items:center;color:#fff;font-size:.6rem;font-weight:800;flex:none}
.mhead b{font-size:.62rem;color:#fff;display:block}
.mhead span{font-size:.5rem;color:#2dd4bf}
.mbolt{margin-left:auto;width:16px;height:16px}
.mbody{flex:1;padding:8px 8px 4px;display:flex;flex-direction:column;gap:6px;overflow:hidden}
.mb{max-width:82%;padding:7px 10px;border-radius:16px;font-size:.6rem;line-height:1.4;animation:popIn .4s both}
.mb.out{align-self:flex-end;background:linear-gradient(90deg,#0084ff,#00c6ff);color:#fff;border-bottom-right-radius:4px}
.mb.in{align-self:flex-start;background:#262a30;color:#e8ecf8;border-bottom-left-radius:4px}
.minput{display:flex;align-items:center;gap:6px;margin:6px 8px 12px;padding:6px 10px;border-radius:999px;background:#262a30}
.minput i{flex:1;font-style:normal;font-size:.55rem;color:#8a8f98}
.minput svg{width:14px;height:14px;flex:none}
'''
if '.devwrap{' not in css:
    css += add
open('hero.css', 'w', encoding='utf-8').write(css)

c = open('index.html', encoding='utf-8').read()
c = c.replace('<img src="img/orange.png" alt="" onerror="this.style.display=\'none\'">', '<span class="lgw"><img src="img/orange.png" alt="" onerror="this.style.display=\'none\'"></span>')
c = c.replace('<img src="img/mvola.png" alt="" onerror="this.style.display=\'none\'">', '<span class="lgw z1"><img src="img/mvola.png" alt="" onerror="this.style.display=\'none\'"></span>')
c = c.replace('<img src="img/airtel.png" alt="" onerror="this.style.display=\'none\'">', '<span class="lgw"><img src="img/airtel.png" alt="" onerror="this.style.display=\'none\'"></span>')
c = c.replace('<img src="img/paypal.png" alt="" onerror="this.style.display=\'none\'">', '<span class="lgw z2"><img src="img/paypal.png" alt="" onerror="this.style.display=\'none\'"></span>')

old_phone = '<div class="phone"><i class="btn-l1"></i><i class="btn-l2"></i><i class="btn-l3"></i><i class="btn-r"></i><div class="screen"><i class="island"></i><div class="ph-head">Agent Logiplus+ • en ligne</div><div class="ph-body"><div class="msg client">Bonjour ! Je cherche un logiciel de design</div><div class="msg agent" id="chatLoop">Bonjour ! Photoshop 2026 est disponible</div></div><i class="homebar"></i></div></div>'
new_tab = '<div class="devwrap"><div class="tab"><i class="cam"></i><div class="scr"><div class="mhead"><span class="mava">L</span><div><b>Agent Logiplus+</b><span>Actif maintenant</span></div><svg class="mbolt" viewBox="0 0 24 24"><path d="M12 2C6.5 2 2 6.2 2 11.4c0 2.9 1.4 5.5 3.6 7.2V22l3.4-1.9c.9.3 1.9.4 3 .4 5.5 0 10-4.2 10-9.4S17.5 2 12 2zm1.1 12.3-2.6-2.7-5 2.7 5.5-5.8 2.6 2.7 5-2.7-5.5 5.8z" fill="#0084ff"/></svg></div><div class="mbody"><div class="mb out">Bonjour ! Je cherche un logiciel de design</div><div class="mb in" id="chatLoop">Bonjour ! Photoshop 2026 est disponible</div></div><div class="minput"><i>Message…</i><svg viewBox="0 0 24 24"><path d="M2 21l21-9L2 3v7l15 2-15 2v7z" fill="#0084ff"/></svg></div><i class="hb"></i></div></div></div>'
if old_phone in c:
    c = c.replace(old_phone, new_tab)
    print('OK - tablette iPad realiste + Messenger + logos mitovy')
else:
    print('TADIO: phone block tsy hita')
open('index.html', 'w', encoding='utf-8').write(c)
