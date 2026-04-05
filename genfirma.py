import os
import markdown
import subprocess

# === KONSTANTY ===
MARKDOWN_DIR = 'mdfirma'
INDEX_FILE = 'index.html'

# === VYTVOR SLOŽKY PRO HTML ===
os.makedirs('html', exist_ok=True)

# === ZJISTI DATUM POSLEDNÍ ÚPRAVY ===
def get_git_last_modified_date(file_path):
    try:
        output = subprocess.check_output(['git', 'log', '-1', '--format=%cd', '--', file_path])
        return output.decode('utf-8').strip()
    except subprocess.CalledProcessError:
        return 'Neznámé'

# === GIT PULL ===
try:
    subprocess.run(['git', 'pull', 'origin', 'main'], check=True)
    print("✅ Aktualizace z GitHubu proběhla.")
except subprocess.CalledProcessError:
    print("⚠ Nepodařilo se provést git pull.")

# === ZPRACUJ .md SOUBORY ===
files_html = []
for md_file in sorted(os.listdir(MARKDOWN_DIR)):
    if not md_file.endswith('.md'):
        continue

    name_with_ext = os.path.splitext(md_file)[0]
    number, name = name_with_ext.split('_', 1)

    md_path = os.path.join(MARKDOWN_DIR, md_file)

    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    html = markdown.markdown(text, extensions=['fenced_code', 'tables'])

    html_file = f"{name_with_ext}.html"
    html_path = os.path.join('html', html_file)

    # === PODSTRÁNKA ===
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(f'''<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name}</title>

<style>
:root {{
  --bg: #ffffff;
  --text: #111;
  --primary: #007BFF;
}}

body.dark {{
  --bg: #121212;
  --text: #eee;
  --primary: #4da3ff;
}}

body {{
  font-family: sans-serif;
  background: var(--bg);
  color: var(--text);
  max-width: 800px;
  margin: auto;
  padding: 1em;
  font-size: 18px;
  line-height: 1.6;
}}

a {{
  color: var(--primary);
}}

#top {{
  display: flex;
  justify-content: space-between;
  align-items: center;
}}

button {{
  padding: 0.5em 1em;
  border: none;
  background: var(--primary);
  color: white;
  border-radius: 6px;
  cursor: pointer;
}}
</style>
</head>

<body>

<div id="top">
  <a href="../{INDEX_FILE}">← Zpět</a>
  <button onclick="toggleDark()">🌙</button>
</div>

<hr>

{html}

<script>
function toggleDark() {{
  document.body.classList.toggle('dark');
  localStorage.setItem('dark-mode', document.body.classList.contains('dark'));
}}

if (localStorage.getItem('dark-mode') === 'true') {{
  document.body.classList.add('dark');
}}
</script>

</body>
</html>''')

    files_html.append({
        'number': int(number),
        'name': name.upper(),
        'file': html_file
    })

# === INDEX ===
with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(f'''<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Firemní stránka</title>

<style>
:root {{
  --bg: #ffffff;
  --text: #111;
  --card: #f5f5f5;
  --primary: #007BFF;
}}

body.dark {{
  --bg: #121212;
  --text: #eee;
  --card: #1e1e1e;
  --primary: #4da3ff;
}}

body {{
  font-family: sans-serif;
  background: var(--bg);
  color: var(--text);
  margin: auto;
  padding: 1em;
  max-width: 1000px;
}}

#top-bar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
}}

h1 {{
  font-size: 1.6em;
}}

h2 {{
  font-size: 1.2em;
  margin-bottom: 1em;
}}

#toggle-dark {{
  cursor: pointer;
  padding: 0.5em 1em;
  border: none;
  background: var(--primary);
  color: white;
  border-radius: 6px;
}}

#cards-container {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
}}

.card {{
  background: var(--card);
  padding: 1em;
  border-radius: 10px;
  cursor: pointer;
  transition: 0.2s;
  font-weight: bold;
  text-align: center;
}}

.card:hover {{
  transform: translateY(-3px);
  background: var(--primary);
  color: white;
}}
</style>
</head>

<body>

<div id="top-bar">
  <h1>🤖 Ing. Libor Kocián</h1>
  <button id="toggle-dark">🌙</button>
</div>

<h2>💡 Automatizace • Digitalizace • Inovace</h2>

<div id="cards-container">
''')

    for file in sorted(files_html, key=lambda x: x['number']):
        f.write(f'''
<div class="card" onclick="window.location.href='html/{file['file']}'">
  {file['name']}
</div>
''')

    f.write('''
</div>

<script>
const toggleBtn = document.getElementById('toggle-dark');

toggleBtn.addEventListener('click', () => {
  document.body.classList.toggle('dark');
  localStorage.setItem('dark-mode', document.body.classList.contains('dark'));
});

if (localStorage.getItem('dark-mode') === 'true') {
  document.body.classList.add('dark');
}
</script>

</body>
</html>
''')

# === GIT PUSH ===
try:
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Zjednodušení UI – odstraněno vyhledávání'], check=True)
    subprocess.run(['git', 'push'], check=True)
    print("✅ Změny odeslány na GitHub.")
except subprocess.CalledProcessError:
    print("⚠ Git commit/push selhal – možná nejsou změny.")
