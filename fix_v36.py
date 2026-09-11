import re
c = open('index.html', encoding='utf-8').read()

# 1. Dika ho an'ny admin.html (talohan'ny fanovana)
admin = c

# 2. index.html : fafao ny lien admin rehetra (nav, menu, footer) + redirect
c2, n1 = re.subn(r'<a[^>]*href="#/admin"[^>]*>.*?</a>', '', c, flags=re.S)
c2 = c2.replace('<head>', '<head><script>if(location.hash.indexOf("#/admin")===0){location.replace("admin.html")}</script>', 1)
open('index.html', 'w', encoding='utf-8').write(c2)
print('OK index.html : ' + str(n1) + ' lien admin voafafa (site madio)')

# 3. admin.html : force route admin + title
admin, n2 = re.subn(r'<a[^>]*href="#/admin"[^>]*>.*?</a>', '', admin, flags=re.S)
admin = re.sub(r'<title>(.*?)</title>', r'<title>Admin \1</title>', admin, count=1)
admin = admin.replace('</head>', '<script>if(!location.hash||location.hash==="#/"||location.hash==="#"){history.replaceState(null,"","#/admin")}</script></head>', 1)
open('admin.html', 'w', encoding='utf-8').write(admin)
print('OK admin.html : pejy admin misaraka')
