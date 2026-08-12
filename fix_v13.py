p = open('pay.js', encoding='utf-8').read()
if 'autoCloseDrawer' not in p:
    p += '''
/* autoCloseDrawer */
document.addEventListener('click',function(e){var d=document.querySelector('.drawer');if(!d||!d.classList.contains('open'))return;if(e.target.closest('.drawer')||e.target.closest('.pm-fab'))return;window.closeDrawer();},true);
'''
    open('pay.js', 'w', encoding='utf-8').write(p)

css = open('pay.css', encoding='utf-8').read()
if '.drawer{top:74px' not in css:
    css += '\n.drawer{top:74px!important}\n'
    open('pay.css', 'w', encoding='utf-8').write(css)
print('OK - panier auto-close + header hita')
