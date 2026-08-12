css = open('hero.css', encoding='utf-8').read()

css = css.replace('.stage{position:relative;max-width:860px;margin:0 auto 26px;height:380px;', '.stage{position:relative;max-width:860px;margin:0 auto 26px;aspect-ratio:16/9;min-height:340px;')
css = css.replace('@media(max-width:640px){.stage{height:360px}}', '@media(max-width:640px){.stage{min-height:330px}}')

old_phone = '''.phone{position:relative;width:180px;height:300px;border-radius:26px;border:2px solid rgba(255,255,255,.28);background:rgba(5,8,15,.92);box-shadow:0 20px 60px -20px rgba(0,0,0,.85),0 0 30px rgba(56,189,248,.3);overflow:hidden;display:flex;flex-direction:column;flex:none}
.phone::before{content:'';position:absolute;top:6px;left:50%;transform:translateX(-50%);width:64px;height:10px;border-radius:999px;background:#000;z-index:2}
.ph-head{padding:20px 10px 6px;text-align:center;font-size:.6rem;font-weight:800;color:#7dd3fc;text-transform:uppercase;letter-spacing:.08em}'''

new_phone = '''.phone{position:relative;width:196px;height:340px;border-radius:36px;background:linear-gradient(145deg,#3a3f4a,#14161a 40%,#0a0c10);padding:6px;box-shadow:0 24px 70px -20px rgba(0,0,0,.9),0 0 0 1px rgba(255,255,255,.14),0 0 34px rgba(56,189,248,.28);flex:none}
.phone .screen{position:relative;width:100%;height:100%;border-radius:30px;background:linear-gradient(180deg,#0b1222,#05070f);overflow:hidden;display:flex;flex-direction:column}
.island{position:absolute;top:10px;left:50%;transform:translateX(-50%);width:66px;height:18px;border-radius:999px;background:#000;box-shadow:inset 0 0 4px rgba(255,255,255,.15);z-index:5}
.island::after{content:'';position:absolute;right:5px;top:6px;width:6px;height:6px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#3b82f6,#0b1222 70%)}
.btn-r{position:absolute;right:-3px;top:96px;width:3px;height:54px;border-radius:2px;background:linear-gradient(90deg,#5a5f68,#23262c)}
.btn-l1{position:absolute;left:-3px;top:72px;width:3px;height:24px;border-radius:2px;background:linear-gradient(90deg,#23262c,#5a5f68)}
.btn-l2{position:absolute;left:-3px;top:106px;width:3px;height:28px;border-radius:2px;background:linear-gradient(90deg,#23262c,#5a5f68)}
.btn-l3{position:absolute;left:-3px;top:140px;width:3px;height:28px;border-radius:2px;background:linear-gradient(90deg,#23262c,#5a5f68)}
.homebar{position:absolute;bottom:6px;left:50%;transform:translateX(-50%);width:72px;height:4px;border-radius:999px;background:rgba(255,255,255,.35)}
.ph-head{padding:34px 10px 6px;text-align:center;font-size:.6rem;font-weight:800;color:#7dd3fc;text-transform:uppercase;letter-spacing:.08em}
@media(max-width:640px){.phone{width:164px;height:286px}}'''

css = css.replace(old_phone, new_phone)
open('hero.css','w',encoding='utf-8').write(css)

c = open('index.html', encoding='utf-8').read()
old_p = '<div class="phone"><div class="ph-head">Agent Logiplus+ • en ligne</div><div class="ph-body"><div class="msg client">Bonjour ! Je cherche un logiciel de design</div><div class="msg agent" id="chatLoop">Bonjour ! Photoshop 2026 est disponible</div></div></div>'
new_p = '<div class="phone"><i class="btn-l1"></i><i class="btn-l2"></i><i class="btn-l3"></i><i class="btn-r"></i><div class="screen"><i class="island"></i><div class="ph-head">Agent Logiplus+ • en ligne</div><div class="ph-body"><div class="msg client">Bonjour ! Je cherche un logiciel de design</div><div class="msg agent" id="chatLoop">Bonjour ! Photoshop 2026 est disponible</div></div><i class="homebar"></i></div></div>'
c = c.replace(old_p, new_p)
open('index.html','w',encoding='utf-8').write(c)
print('OK - 16:9 + iPhone réaliste')
