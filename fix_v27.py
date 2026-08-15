import re

base = 'https://cshmobqykkqjmusnkeom.supabase.co/functions/v1/tg?p='
upload = 'https://cshmobqykkqjmusnkeom.supabase.co/functions/v1/tg-upload'

# 1. app1.js : getImageUrl() + admin upload
a = open('app1.js', encoding='utf-8').read()

# Ampidiro ny helper getImageUrl raha tsy misy
if 'window.getImageUrl' not in a:
    a = 'window.PROXY="' + base + '";window.UPLOAD="' + upload + '";window.getImageUrl=function(p){if(!p||p.length<2)return "";if(p.startsWith("http"))return p;return window.PROXY+p};\n' + a
else:
    a = re.sub(r"window\.PROXY='[^']*';", "window.PROXY='" + base + "';", a)

# 2. Rehefa mampiseho ny sary amin'ny card, mampiasa getImageUrl
a = re.sub(r'item\.image\s*\|\|\s*["\']["\']\s*,\s*["\']([^"\']*)["\']', r'getImageUrl(item.image)||"$1"', a)
a = re.sub(r"<img[^>]*src=['\"]?([^'\"]*?)['\"]?[^>]*>", lambda m: m.group(0).replace('item.image', 'getImageUrl(item.image)') if 'item.image' in m.group(0) else m.group(0), a)

# 3. Admin upload function (ao amin'ny admin panel raha misy champ image)
upload_js = '''
window.uploadToTelegram=function(file){
  var fd=new FormData();fd.append('file',file);
  return fetch(window.UPLOAD,{method:'POST',body:fd}).then(function(r){return r.json()}).then(function(d){if(!d.ok)throw new Error(d.err);return d.file_path});
};
'''
if 'uploadToTelegram' not in a:
    a += upload_js

open('app1.js', 'w', encoding='utf-8').write(a)
print('OK app1.js')

# 4. hero.js raha misy renderGrid misy sary
try:
    h = open('hero.js', encoding='utf-8').read()
    if 'item.image' in h and 'getImageUrl' not in h:
        h = 'window.getImageUrl=window.getImageUrl||function(p){if(!p)return "";if(p.startsWith("http"))return p;return (window.PROXY||"' + base + '")+p};\n' + h
        h = re.sub(r'(["\'])img/([^"\']+)\\.png(["\'])', r'\1' + base + r'\2.png\3', h)
        open('hero.js', 'w', encoding='utf-8').write(h)
        print('OK hero.js')
except Exception as e:
    print('hero.js: ' + str(e))

