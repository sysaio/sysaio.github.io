import os
import markdown
import subprocess
from datetime import datetime

# === KONSTANTY ===
MARKDOWN_DIR = 'mdfirma'  # Složka, kde jsou .md soubory
INDEX_FILE = 'index.html'  # Výstupní HTML soubor

# === VYTVOR SLOŽKY PRO HTML ===
os.makedirs('html', exist_ok=True)

# === ZJISTI DATUM POSLEDNÍ ÚPRAVY ===
def get_git_last_modified_date(file_path):
    try:
        output = subprocess.check_output(['git', 'log', '-1', '--format=%cd', '--', file_path])
        return output.decode('utf-8').strip()
    except subprocess.CalledProcessError:
        return 'Neznámé'

# === GIT PULL PŘED SPUŠTĚNÍM ===
try:
    subprocess.run(['git', 'pull', 'origin', 'main'], check=True)
    print("✅ Aktualizace z GitHubu proběhla.")
except subprocess.CalledProcessError:
    print("⚠ Nepodařilo se provést git pull.")

# === ZPRACUJ VŠECHNY .md SOUBORY ===
files_html = []
for md_file in sorted(os.listdir(MARKDOWN_DIR)):
    if not md_file.endswith('.md'):
        continue

    # Extrakce čísla a textu ze souboru
    name_with_ext = os.path.splitext(md_file)[0]  # Např. '01_uvod'
    number, name = name_with_ext.split('_', 1)  # Rozdělí na číslo a text

    md_path = os.path.join(MARKDOWN_DIR, md_file)

    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    html = markdown.markdown(text, extensions=['fenced_code', 'tables'])
    last_modified = get_git_last_modified_date(md_path)

    html_file = f"{name_with_ext}.html"
    html_path = os.path.join('html', html_file)

    # Uložení HTML souboru pro každý .md soubor
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(f'''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>{name}</title></head>
<body>
{html}
<p><a href="../{INDEX_FILE}">← Zpět na přehled</a></p>
</body>
</html>''')

    files_html.append({
        'number': int(number),  # Uložení čísla pro správné řazení
        'name': name.upper(),  # Text na tlačítku (velkými písmeny)
        'file': html_file,
        'last_modified': last_modified
    })

# === GENERUJ index.html ===
with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(f'''<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <title>Firemní stránka</title>
  <style>
    body {{ font-family: sans-serif; max-width: 1000px; margin: auto; padding: 2em; }}
    button {{ 
        padding: 0.6em 1.2em; 
        background-color: #007BFF;  /* Modrá barva */
        color: white; 
        border: none; 
        border-radius: 5px; 
        cursor: pointer;
        margin: 10px;
        font-size: 16px;
        text-align: center;
        transition: background-color 0.3s ease;
    }}
    button:hover {{
        background-color: #0056b3;  /* Tmavší modrá při hover */
    }}
    #search {{
        width: 100%;
        padding: 0.5em;
        margin-bottom: 20px;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
    }}
    th, td {{
        padding: 0.8em;
        text-align: left;
        border: 1px solid #ddd;
    }}
    th {{
        background-color: #f2f2f2;
    }}
  </style>
</head>
<body>
  <h1>🤖 Ing. Libor Kocián - Chytrá řešení pro automatizaci, digitalizaci, inovace⚙️</h1>
  <h2>💡 Poznejte možnosti automatizace a inovací ve vašich procesech
– první analýza a návrh chytrých řešení ZDARMA!</h2>

  <input type="text" id="search" placeholder="🔍 Hledat...">

  <div id="buttons-container">
''')

    # Seřazení souborů podle čísla a generování tlačítek
    for file in sorted(files_html, key=lambda x: x['number']):
        f.write(f'''      <button onclick="window.location.href='html/{file['file']}'">{file['name']}</button>\n''')

    f.write('''
  </div>

  <script>
    const searchInput = document.getElementById('search');
    const buttons = document.querySelectorAll('button');

    searchInput.addEventListener('input', function () {
      const query = this.value.toLowerCase();
      buttons.forEach(button => {
        const text = button.innerText.toLowerCase();
        button.style.display = text.includes(query) ? '' : 'none';
      });
    });
  </script>
</body>
</html>
''')

# === GIT COMMIT A PUSH ===
try:
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Automatická aktualizace firemní stránky'], check=True)
    subprocess.run(['git', 'push'], check=True)
    print("✅ Změny odeslány na GitHub.")
except subprocess.CalledProcessError:
    print("⚠ Git commit/push selhal – možná nejsou žádné změny.")
