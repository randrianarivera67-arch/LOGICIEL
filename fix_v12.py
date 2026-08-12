css = open('hero.css', encoding='utf-8').read()
add = '''
.hero{padding:6px 0 0!important}
.hero .search{margin-bottom:10px}
.stage-kicker{margin:0 auto 10px}
.stage{margin:0 auto 16px}
.toolbar{margin-top:0!important}
'''
if '.hero{padding:6px 0 0!important}' not in css:
    css += add
    open('hero.css', 'w', encoding='utf-8').write(css)
print('OK - espaces retrecis')
