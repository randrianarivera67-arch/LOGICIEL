b = open('admin.js', encoding='utf-8').read()

# 1. Ny container-n'ny Exporter/Importer/Reset/Quitter -> horizontal scroll
old = "var menu=document.createElement('div');menu.id='admMenu';"
new = """var _eb=[].slice.call(ap.querySelectorAll('button,label')).filter(function(x){return x.textContent.indexOf('Exporter')>-1})[0];
if(_eb&&_eb.parentNode&&_eb.parentNode!==ap){var _w=_eb.parentNode;_w.style.cssText+=';display:flex;flex-wrap:nowrap;overflow-x:auto;gap:8px;scrollbar-width:none;-webkit-overflow-scrolling:touch;padding-bottom:4px';}
var menu=document.createElement('div');menu.id='admMenu';"""
if old in b:
    b = b.replace(old, new, 1)
    print('OK container horizontal')
else:
    print('!! tsy hita ny menu marker')

# 2. Button kely kokoa ao amin'ny view-admin rehetra
old2 = "document.head.appendChild(st);"
new2 = "var st2=document.createElement('style');st2.textContent='#view-admin .btn{padding:8px 13px;font-size:.78rem;border-radius:10px;flex:none;white-space:nowrap}#view-admin .adm-sec .btn{padding:8px 13px;font-size:.78rem}';document.head.appendChild(st2);document.head.appendChild(st);"
if old2 in b:
    b = b.replace(old2, new2, 1)
    print('OK btn kely')

open('admin.js', 'w', encoding='utf-8').write(b)
print('OK admin.js v32')
