import re
files = ['app1.js', 'app2.js', 'pay.js', 'hero.js', 'theme.js', 'main.js']
for f in files:
    try:
        c = open(f, encoding='utf-8').read()
    except Exception:
        continue
    o = c
    c = re.sub(r"(\|\|\s*)['\"]dark['\"]", r"\1'light'", c)
    c = re.sub(r'if\s*\(\s*!t\s*\)\s*t\s*=\s*[\'"]dark[\'"]', "if(!t)t='light'", c)
    if c != o:
        open(f, 'w', encoding='utf-8').write(c)
        print('OK - ' + f + ' : clair par defaut')
    for i, line in enumerate(c.splitlines()):
        if 'theme' in line.lower() and ('dark' in line or 'light' in line):
            print(f + ':' + str(i) + ': ' + line.strip()[:100])
