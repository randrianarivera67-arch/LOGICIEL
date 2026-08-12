import re

with open('pay.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Soloina ny farany mba hanisy polling
old_end = """window.addEventListener('hashchange',function(){setTimeout(injectSettings,300)});
setTimeout(function(){renderDrawer();injectSettings()},600);
})();"""

new_end = """window.addEventListener('hashchange',function(){setTimeout(injectSettings,300)});
setTimeout(function(){renderDrawer();injectSettings()},600);
var pollInterval=setInterval(function(){var ap=document.getElementById('adminPanel');if(ap&&!ap.hidden&&!document.getElementById('paySettings')){injectSettings()}},800);
setTimeout(function(){clearInterval(pollInterval)},30000);
})();"""

content = content.replace(old_end, new_end)

with open('pay.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK - polling ajouté')
