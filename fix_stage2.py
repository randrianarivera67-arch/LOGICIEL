css = '''.stage-kicker{font-family:Sora,sans-serif;font-weight:700;font-size:clamp(.95rem,2.6vw,1.3rem);color:var(--text);margin:4px auto 16px;max-width:860px;text-align:center;letter-spacing:.02em}
.stage{position:relative;max-width:860px;margin:0 auto 26px;height:360px;border-radius:24px;border:1px solid var(--border);overflow:hidden;background:#05070f}
.stage::after{content:'';position:absolute;inset:-6%;background:url("img/stage-bg.png") center/cover no-repeat;animation:kb 26s ease-in-out infinite alternate;z-index:0}
@keyframes kb{from{transform:scale(1) translate(0,0)}to{transform:scale(1.14) translate(-2%,2%)}}
.stage::before{content:'';position:absolute;inset:0;z-index:1;background:linear-gradient(120deg,rgba(56,189,248,.22),rgba(244,63,94,.16),rgba(139,92,246,.24),rgba(45,212,191,.2));background-size:300% 300%;animation:gradMove 12s ease infinite;mix-blend-mode:screen}
body.light .stage::before{mix-blend-mode:multiply;background:linear-gradient(120deg,rgba(2,6,23,.6),rgba(15,23,42,.5),rgba(2,6,23,.6));background-size:300% 300%}
@keyframes gradMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
@media(max-width:640px){.stage{height:340px}}
.iscene{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:20px;opacity:0;transform:scale(.97);transition:opacity .7s,transform .7s;text-align:center;z-index:3}
.iscene.on{opacity:1;transform:scale(1)}
.iscene h2{font-family:Sora,sans-serif;font-size:clamp(1.4rem,4vw,2.4rem);font-weight:800;color:#fff;text-shadow:0 4px 24px rgba(0,0,0,.75)}
.iscene p{color:#dbe6f5;font-size:.92rem;max-width:520px;text-shadow:0 2px 12px rgba(0,0,0,.65)}
.ilogo{width:64px;height:64px;filter:drop-shadow(0 0 18px rgba(56,189,248,.8))}
.iimg{max-height:210px;max-width:78%;border-radius:16px;border:1px solid rgba(255,255,255,.2);box-shadow:0 30px 70px -25px rgba(37,99,235,.65)}
.chat-b{position:absolute;background:rgba(5,8,15,.85);border:1px solid rgba(255,255,255,.15);border-radius:14px;padding:9px 13px;font-size:.78rem;max-width:70%;box-shadow:0 10px 30px -10px rgba(0,0,0,.6);animation:popIn .5s both;text-align:left;color:#e8ecf8}
.chat-b .who{display:block;font-size:.6rem;font-weight:800;margin-bottom:3px;text-transform:uppercase;letter-spacing:.08em;color:#7dd3fc}
.chat-b.client{right:5%;top:8%;border-bottom-right-radius:4px}
.chat-b.agent{left:5%;bottom:10%;border-bottom-left-radius:4px;border-color:rgba(45,212,191,.45)}
.chat-b.agent .who{color:#2dd4bf}
@keyframes popIn{from{opacity:0;transform:scale(.85) translateY(10px)}to{opacity:1;transform:scale(1) translateY(0)}}
.typing{display:inline-flex;gap:4px}
.typing i{width:6px;height:6px;border-radius:50%;background:#93a0b8;animation:tp 1s infinite}
.typing i:nth-child(2){animation-delay:.2s}
.typing i:nth-child(3){animation-delay:.4s}
@keyframes tp{0%,100%{opacity:.3;transform:translateY(0)}50%{opacity:1;transform:translateY(-3px)}}
.ifeats{display:flex;gap:12px;flex-wrap:wrap;justify-content:center}
.ifeat.pay{display:flex;flex-direction:column;align-items:center;gap:8px;padding:12px 16px;border-radius:16px;border:1px solid rgba(255,255,255,.15);background:rgba(5,8,15,.7);color:#e8ecf8;font-size:.78rem;font-weight:600;opacity:0;transform:translateY(12px);transition:.5s}
.ifeat.pay.on{opacity:1;transform:translateY(0)}
.ifeat.pay img{width:44px;height:44px;border-radius:10px;object-fit:cover}
.tw2::after{content:'';display:inline-block;width:2px;height:1em;background:#7dd3fc;vertical-align:-2px;margin-left:3px;animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
.spark{position:absolute;width:6px;height:6px;border-radius:50%;background:#fff;opacity:0;animation:spop linear infinite;z-index:2;box-shadow:0 0 8px 2px rgba(255,255,255,.5)}
.spark:nth-child(3n){background:#38bdf8;box-shadow:0 0 10px 3px rgba(56,189,248,.6)}
.spark:nth-child(3n+1){background:#f43f5e;box-shadow:0 0 10px 3px rgba(244,63,94,.6)}
.spark:nth-child(3n+2){background:#8b5cf6;box-shadow:0 0 10px 3px rgba(139,92,246,.6)}
@keyframes spop{0%{transform:scale(0);opacity:0}20%{opacity:1}50%{transform:scale(1.5);opacity:.9}100%{transform:scale(0);opacity:0}}
.femo{position:absolute;font-size:1.15rem;opacity:.4;animation:drift 7s ease-in-out infinite;z-index:2;filter:drop-shadow(0 0 6px rgba(56,189,248,.7))}
@keyframes drift{0%,100%{transform:translateY(0) rotate(-5deg);opacity:.3}50%{transform:translateY(-18px) rotate(7deg);opacity:.85}}
.burst{position:absolute;left:50%;top:50%;width:10px;height:10px;border-radius:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:2;animation:bw .7s ease-out forwards}
@keyframes bw{from{box-shadow:0 0 0 0 rgba(255,255,255,.7),0 0 30px 10px rgba(56,189,248,.5);opacity:1}to{box-shadow:0 0 0 150px rgba(255,255,255,0),0 0 60px 30px rgba(139,92,246,0);opacity:0}}'''

c = open('index.html', encoding='utf-8').read()
c = c.replace('<div class="sbar"><i id="stageBar"></i></div>', '')
if 'stage-kicker' not in c:
    c = c.replace('<div class="stage" id="stage">', '<p class="stage-kicker">✨ Découvrez <span class="grad">vos logiciels préférés</span> sur notre plateforme ✨</p>\n<div class="stage" id="stage">')
open('hero.css','w',encoding='utf-8').write(css)
open('index.html','w',encoding='utf-8').write(c)
print('OK - sary + kicker + tsy misy ligne')
