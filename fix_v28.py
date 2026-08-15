import re

base = 'https://cshmobqykkqjmusnkeom.supabase.co/functions/v1/tg?p='
upload = 'https://cshmobqykkqjmusnkeom.supabase.co/functions/v1/tg-upload'

a = open('admin.js', encoding='utf-8').read()
o = a

# 1. Ampidiro ny helpers raha tsy misy
helpers = f'''
window.PROXY="{base}";
window.UPLOAD="{upload}";
window.getImageUrl=function(p){{if(!p||p.length<2)return "";if(p.startsWith("http"))return p;return window.PROXY+p;}};
window.uploadToTelegram=function(file){{
  var fd=new FormData();fd.append('file',file);
  return fetch(window.UPLOAD,{{method:'POST',body:fd}}).then(function(r){{return r.json()}}).then(function(d){{
    if(!d.ok)throw new Error(d.err||"Upload failed");return d.file_path;
  }});
}};
'''
if 'window.getImageUrl' not in a:
    a = helpers + a

# 2. Ovay ny render sary (raha misy item.image)
a = re.sub(r'(["\'])img/([^"\']+)\\.png(["\'])', r'\1' + base + r'\2.png\3', a)
a = re.sub(r'src=["\']([^"\']*?)item\.image([^"\']*?)["\']', r'src="$1getImageUrl(item.image)$2"', a)
a = re.sub(r'src=["\']([^"\']*?)p\.image([^"\']*?)["\']', r'src="$1getImageUrl(p.image)$2"', a)

# 3. Ovay ny <input type="file"> amin'ny formulaire image raha misy
# Manampy bouton Upload auto raha misy champ image
a = re.sub(
    r'(<input[^>]*id=["\']([^"\']*image[^"\']*)["\'][^>]*type=["\']text["\'][^>]*>)',
    r'\1<input type="file" id="\2_upload" accept="image/*" onchange="(async()=>{try{toast(\'⏳ Upload...\');var p=await uploadToTelegram(this.files[0]);document.getElementById(\'\2\').value=p;toast(\'✅ \'+p)}catch(e){toast(\'❌ \'+e.message)}}).call(this)"/>',
    a
)

if a != o:
    open('admin.js', 'w', encoding='utf-8').write(a)
    print('OK admin.js - upload Telegram + getImageUrl')
else:
    print('Tsy nisy fanovana')

