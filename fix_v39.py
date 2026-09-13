import re

h = open('admin.html', encoding='utf-8').read()

# Auto-update check script
update_script = '''
<script>
(function(){
  var CURRENT_VERSION = "1.0.0";
  var UPDATE_URL = "https://raw.githubusercontent.com/randrianarivera67-arch/LOGICIEL/main/version.json";
  
  function checkUpdate(){
    fetch(UPDATE_URL + "?t=" + Date.now())
      .then(function(r){return r.json()})
      .then(function(data){
        if(data.version !== CURRENT_VERSION){
          var msg = "Version vaovao hita: " + data.version + "\\nTsindrio OK hisintona ny APK vaovao.";
          if(confirm(msg)){
            window.open(data.download_url, "_system");
          }
        }
      })
      .catch(function(){});
  }
  
  // Check isaky ny 1 ora
  setTimeout(checkUpdate, 5000);
  setInterval(checkUpdate, 3600000);
})();
</script>
'''

if 'checkUpdate' not in h:
    h = h.replace('</head>', update_script + '</head>')
    open('admin.html', 'w', encoding='utf-8').write(h)
    print('OK auto-update script')
else:
    print('Efa misy auto-update')

# version.json
import json
version = {"version": "1.0.0", "download_url": "https://github.com/randrianarivera67-arch/LOGICIEL/releases/latest/download/admin.apk"}
open('version.json', 'w').write(json.dumps(version, indent=2))
print('OK version.json')
