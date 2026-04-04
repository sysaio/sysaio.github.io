import os
import subprocess

# Cesta k adresáři s .md soubory
md_dir = "mdfirma"  # Nastav si vlastní cestu

# Funkce pro generování HTML
def generate_html(md_files):
    html_content = """
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Firemní stránka</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 50px;
        }
        .button {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 20px;
            margin: 10px;
            cursor: pointer;
            border-radius: 5px;
        }
        .button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Firemní dokumentace</h1>
    <div>
"""
    for md_file in md_files:
        name = md_file.replace(".md", "").upper()  # Velká písmena
        html_content += f'<button class="button" onclick="window.location.href=\'{md_file}\';">{name}</button>\n'

    html_content += """
    </div>
</body>
</html>
"""
    return html_content

# Funkce pro provedení git commit a push
def git_commit_and_push():
    try:
        # Přidáme všechny změny a nový index.html
        subprocess.run(["git", "add", "."], check=True)
        # Commit s zprávou
        subprocess.run(["git", "commit", "-m", "Automatický update firemní stránky"], check=True)
        # Push na GitHub
        subprocess.run(["git", "push"], check=True)
        print("Změny byly úspěšně pushnuty na GitHub!")
    except subprocess.CalledProcessError as e:
        print(f"Chyba při git operacích: {e}")

# Získání seznamu .md souborů
def get_md_files(directory):
    return [f for f in os.listdir(directory) if f.endswith(".md")]

# Hlavní funkce
def main():
    # Získání seznamu .md souborů
    md_files = get_md_files(md_dir)

    # Vygenerování HTML kódu
    index_html = generate_html(md_files)

    # Uložení HTML do souboru
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

    # Provést git commit a push
    git_commit_and_push()

if __name__ == "__main__":
    main()