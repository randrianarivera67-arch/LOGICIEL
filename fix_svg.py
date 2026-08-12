svg_bg = '''data:image/svg+xml;utf8,''' + '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600" preserveAspectRatio="xMidYMid slice"><defs><radialGradient id="g1" cx="50%" cy="50%" r="60%"><stop offset="0%" stop-color="#0ea5e9" stop-opacity=".5"/><stop offset="100%" stop-color="#020617" stop-opacity="0"/></radialGradient><pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M 60 0 L 0 0 0 60" fill="none" stroke="#38bdf8" stroke-width=".6" opacity=".15"/><circle cx="60" cy="0" r="1.5" fill="#38bdf8"/><circle cx="0" cy="60" r="1.5" fill="#38bdf8"/></pattern><linearGradient id="cpu" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1e293b"/><stop offset="100%" stop-color="#0f172a"/></linearGradient></defs><rect width="1200" height="600" fill="#05070f"/><rect width="1200" height="600" fill="url(#grid)"/><rect width="1200" height="600" fill="url(#g1)"/><g transform="translate(300,200)"><rect x="-70" y="-70" width="140" height="140" rx="12" fill="url(#cpu)" stroke="#38bdf8" stroke-width="2"/><rect x="-50" y="-50" width="100" height="100" rx="6" fill="#020617"/><text x="0" y="8" text-anchor="middle" font-family="monospace" font-size="22" font-weight="700" fill="#38bdf8">CPU</text><g stroke="#38bdf8" stroke-width="2" fill="none"><path d="M-70,0 H-120"/><path d="M70,0 H120"/><path d="M0,-70 V-120"/><path d="M0,70 V120"/><path d="M-50,-50 L-90,-90"/><path d="M50,50 L90,90"/><path d="M-50,50 L-90,90"/><path d="M50,-50 L90,-90"/></g><g fill="#38bdf8"><circle cx="-120" cy="0" r="3"/><circle cx="120" cy="0" r="3"/><circle cx="0" cy="-120" r="3"/><circle cx="0" cy="120" r="3"/><circle cx="-90" cy="-90" r="3"/><circle cx="90" cy="90" r="3"/><circle cx="-90" cy="90" r="3"/><circle cx="90" cy="-90" r="3"/></g></g><g stroke="#f43f5e" stroke-width="1.5" fill="none" opacity=".7"><path d="M700,100 H950 L1000,150 V250"><animate attributeName="stroke-dashoffset" from="400" to="0" dur="3s" repeatCount="indefinite"/></path><path d="M1000,250 V350 L950,400 H800"><animate attributeName="stroke-dashoffset" from="400" to="0" dur="3s" begin="1s" repeatCount="indefinite"/></path></g><g fill="#f43f5e" opacity=".8"><circle cx="700" cy="100" r="4"><animate attributeName="opacity" values="0.3;1;0.3" dur="2s" repeatCount="indefinite"/></circle><circle cx="1000" cy="150" r="4"><animate attributeName="opacity" values="0.3;1;0.3" dur="2s" begin=".5s" repeatCount="indefinite"/></circle><circle cx="1000" cy="350" r="4"><animate attributeName="opacity" values="0.3;1;0.3" dur="2s" begin="1s" repeatCount="indefinite"/></circle><circle cx="800" cy="400" r="4"><animate attributeName="opacity" values="0.3;1;0.3" dur="2s" begin="1.5s" repeatCount="indefinite"/></circle></g><g stroke="#8b5cf6" stroke-width="1.2" fill="none" opacity=".6"><path d="M100,450 Q200,420 300,450 T500,450"><animate attributeName="d" values="M100,450 Q200,420 300,450 T500,450;M100,450 Q200,480 300,450 T500,450;M100,450 Q200,420 300,450 T500,450" dur="4s" repeatCount="indefinite"/></path></g><g fill="#2dd4bf" opacity=".9"><circle cx="150" cy="450" r="3"><animate attributeName="cy" values="450;440;450" dur="2s" repeatCount="indefinite"/></circle><circle cx="350" cy="450" r="3"><animate attributeName="cy" values="450;460;450" dur="2s" begin=".7s" repeatCount="indefinite"/></circle></g></svg>'''

css = '''.stage{position:relative;max-width:860px;margin:0 auto 26px;height:360px;border-radius:24px;border:1px solid var(--border);overflow:hidden;background:#05070f}
.stage::after{content:'';position:absolute;inset:-6%;background:url("''' + svg_bg + '''") center/cover no-repeat;animation:kb 26s ease-in-out infinite alternate;z-index:0}
@keyframes kb{from{transform:scale(1) translate(0,0)}to{transform:scale(1.14) translate(-2%,2%)}}
.stage::before{content:'';position:absolute;inset:0;z-index:1;background:linear-gradient(120deg,rgba(56,189,248,.25),rgba(244,63,94,.18),rgba(139,92,246,.28),rgba(45,212,191,.22));background-size:300% 300%;animation:gradMove 12s ease infinite;mix-blend-mode:screen}
body.light .stage::before{mix-blend-mode:multiply;background:linear-gradient(120deg,rgba(2,6,23,.55),rgba(15,23,42,.45),rgba(2,6,23,.55));background-size:300% 300%}
@keyframes gradMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
@media(max-width:640px){.stage{height:340px}}
.sbar{position:absolute;left:0;bottom:0;height:3px;width:100%;background:rgba(255,255,255,.12);z-index:4}
.sbar i{display:block;height:100%;width:0;background:var(--grad)}
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

open('hero.css','w',encoding='utf-8').write(css)
print('OK - SVG circuit inline installé')
