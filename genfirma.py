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

    name = os.path.splitext(md_file)[0]
    md_path = os.path.join(MARKDOWN_DIR, md_file)

    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    html = markdown.markdown(text, extensions=['fenced_code', 'tables'])
    last_modified = get_git_last_modified_date(md_path)

    html_file = f"{name}.html"
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
        'name': name,
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
    button {{ padding: 0.3em 0.6em; }}
  </style>
</head>
<body>
  <h1>📚 Firemní dokumentace</h1>

  <input type="text" id="search" placeholder="🔍 Hledat...">
  <table>
    <thead>
      <tr>
        <th>Návod</th>
        <th>Poslední úprava</th>
      </tr>
    </thead>
    <tbody>
''')

    for file in files_html:
        f.write(f'''      <tr>
        <td><a href="html/{file['file']}">{file['name']}</a></td>
        <td>{file['last_modified']}</td>
      </tr>\n''')

    f.write('''    </tbody>
  </table>

  <script>
    const searchInput = document.getElementById('search');
    const rows = document.querySelectorAll('tbody tr');

    searchInput.addEventListener('input', function () {
      const query = this.value.toLowerCase();
      rows.forEach(row => {
        const text = row.innerText.toLowerCase();
        row.style.display = text.includes(query) ? '' : 'none';
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