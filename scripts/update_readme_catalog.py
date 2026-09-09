import json
import os
import sys

def format_size(bytes_val):
    if not bytes_val:
        return ""
    if bytes_val >= 1024 * 1024:
        return f"{bytes_val / (1024 * 1024):.1f} Mo"
    elif bytes_val >= 1024:
        return f"{bytes_val / 1024:.0f} Ko"
    return f"{bytes_val} o"

def generate_catalog_markdown(catalog_path):
    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    modules = catalog.get("modules", [])

    category_metadata = {
        "bible": {
            "title": "📖 Traductions Bibliques",
            "desc": "Traductions intégrales de l'Ancien et du Nouveau Testament avec indexation textuelle et codes Strong."
        },
        "commentary": {
            "title": "💬 Commentaires Bibliques",
            "desc": "Commentaires verset par verset et analyses exégétiques structurées."
        },
        "theology": {
            "title": "🏛️ Théologie & Dogmatique",
            "desc": "Traités doctrinaux majeurs, théologies systématiques et confessions de foi historiques."
        },
        "dictionary": {
            "title": "📚 Dictionnaires & Encyclopédies",
            "desc": "Lexiques originaux, dictionnaires bibliques encyclopédiques et définitions théologiques."
        },
        "dataset": {
            "title": "🎨 Jeux de Données & Multimédia",
            "desc": "Données multimédias, liens vidéos, affiches HD et métadonnées complémentaires."
        }
    }

    order = ["bible", "commentary", "theology", "dictionary", "dataset"]
    # Include any extra types not explicitly listed
    present_types = []
    for t in order:
        if any(m.get("type") == t for m in modules):
            present_types.append(t)
    for m in modules:
        t = m.get("type", "other")
        if t not in present_types:
            present_types.append(t)

    lines = []
    lines.append("## 📚 Ouvrages & Ressources Disponibles\n")
    lines.append(f"> 💡 Le catalogue compte actuellement **{len(modules)} modules** prêts au téléchargement direct ou via l'API client.\n")

    for cat_type in present_types:
        mods = [m for m in modules if m.get("type") == cat_type]
        if not mods:
            continue

        meta = category_metadata.get(cat_type, {
            "title": f"📦 {cat_type.capitalize()}",
            "desc": f"Ressources de type {cat_type}."
        })

        lines.append(f"### {meta['title']}\n")
        lines.append(f"{meta['desc']}\n")
        lines.append("| Couverture | Module | Code | Auteur / Éditeur | Format & Taille | Licence | Téléchargement |")
        lines.append("| :---: | :--- | :---: | :--- | :---: | :---: | :---: |")

        for m in mods:
            cover_url = m.get("cover_url")
            abbr = m.get("abbreviation", m.get("id", ""))
            if cover_url:
                cover_md = f'<img src="{cover_url}" width="42" alt="{abbr}">'
            else:
                cover_md = "—"

            title_md = f"**{m.get('title', '')}**"
            code_md = f"`{abbr}`"
            author_md = m.get("author", "—")
            
            fmt = m.get("format", "").upper()
            size = format_size(m.get("size_bytes", 0))
            fmt_size = f"{fmt} ({size})" if size else fmt

            lic = m.get("license", "Domaine Public")
            dl_url = m.get("download_url", "")
            dl_md = f"[⬇️ Télécharger]({dl_url})" if dl_url else "—"

            lines.append(f"| {cover_md} | {title_md} | {code_md} | {author_md} | {fmt_size} | {lic} | {dl_md} |")

        lines.append("")

    return "\n".join(lines).strip()

def update_readme(readme_path, catalog_path, check_only=False):
    if not os.path.exists(readme_path):
        print(f"[ERREUR] Le fichier {readme_path} n'existe pas.")
        return False
    if not os.path.exists(catalog_path):
        print(f"[ERREUR] Le fichier {catalog_path} n'existe pas.")
        return False

    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()

    new_section = generate_catalog_markdown(catalog_path)
    start_tag = "<!-- START_CATALOG -->"
    end_tag = "<!-- END_CATALOG -->"

    if start_tag in readme_content and end_tag in readme_content:
        before = readme_content.split(start_tag)[0]
        after = readme_content.split(end_tag)[1]
        updated_content = f"{before}{start_tag}\n\n{new_section}\n\n{end_tag}{after}"
    else:
        # Insert before "## 🚀 Utilisation dans une Application (Client)" or append
        target_marker = "## 🚀 Utilisation dans une Application (Client)"
        if target_marker in readme_content:
            parts = readme_content.split(target_marker)
            updated_content = f"{parts[0]}{start_tag}\n\n{new_section}\n\n{end_tag}\n\n---\n\n{target_marker}{parts[1]}"
        else:
            updated_content = f"{readme_content}\n\n---\n\n{start_tag}\n\n{new_section}\n\n{end_tag}\n"

    if check_only:
        if readme_content.strip() == updated_content.strip():
            print("[OK] Le README.md est à jour avec le catalogue.")
            return True
        else:
            print("[DIFF] Le README.md n'est pas synchronisé avec catalog.json.")
            return False

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"[SUCCÈS] README.md mis à jour avec succès depuis {catalog_path} !")
    return True

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cat_path = os.path.join(base_dir, "catalog.json")
    rdm_path = os.path.join(base_dir, "README.md")
    
    check = "--check" in sys.argv
    success = update_readme(rdm_path, cat_path, check_only=check)
    sys.exit(0 if success else 1)
