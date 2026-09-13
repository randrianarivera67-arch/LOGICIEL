#!/bin/bash
echo "🚀 Batch reupload sary Telegram"
echo ""
echo "📋 Produits 16:"
python3 sary_tracker.py

echo ""
echo "🔧 FOMBA:"
echo "1. Mamorona dossier 'sary/' ao amin'ny ~/LOGICIEL"
echo "2. Copy ny 16 sary ao amin'ny sary/"
echo "3. Alefaso ity script ity:"
echo ""
cat <<'EOF'
for img in sary/*.jpg sary/*.jpeg sary/*.png; do
  [ -f "$img" ] || continue
  name=$(basename "$img")
  echo "📤 Upload: $name"
  curl -s -X POST "https://cshmobqykkqjmusnkeom.supabase.co/functions/v1/tg-upload" \
    -F "file=@$img" | grep -o '"file_path":"[^"]*"' || echo "❌ Diso: $name"
done
EOF
