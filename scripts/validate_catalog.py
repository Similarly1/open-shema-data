#!/usr/bin/env python3
"""
Script de validation pour catalog.json dans open-shema-data.
Vérifie la syntaxe JSON, les champs obligatoires, l'unicité des identifiants et les formats.
"""

import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def validate_catalog(catalog_path="catalog.json", schema_path="schemas/catalog.schema.json"):
    if not os.path.exists(catalog_path):
        print(f"[ERREUR] Le fichier {catalog_path} n'existe pas.")
        return False

    with open(catalog_path, "r", encoding="utf-8") as f:
        try:
            catalog = json.load(f)
        except Exception as e:
            print(f"[ERREUR] Erreur de syntaxe JSON dans {catalog_path}: {e}")
            return False

    required_top = ["catalog_version", "name", "updated_at", "modules"]
    for field in required_top:
        if field not in catalog:
            print(f"[ERREUR] Champ racine manquant: '{field}'")
            return False

    modules = catalog.get("modules", [])
    print(f"[INFO] Validation de {len(modules)} module(s)...")

    ids = set()
    valid_types = {"bible", "dictionary", "commentary", "theology", "dataset", "cross_references", "maps"}
    valid_formats = {"sqlite", "json", "sqlite.gz", "json.gz"}

    errors = 0
    for idx, mod in enumerate(modules):
        mod_id = mod.get("id")
        if not mod_id:
            print(f"[ERREUR] [Module #{idx}] 'id' manquant.")
            errors += 1
            continue

        if mod_id in ids:
            print(f"[ERREUR] [Module {mod_id}] Identifiant en double !")
            errors += 1
        ids.add(mod_id)

        # Required fields
        for req in ["type", "title", "language", "format", "version", "download_url"]:
            if req not in mod:
                print(f"[ERREUR] [Module {mod_id}] Champ obligatoire manquant : '{req}'")
                errors += 1

        # Validation type & format
        if mod.get("type") not in valid_types:
            print(f"[ERREUR] [Module {mod_id}] Type invalide '{mod.get('type')}'. Attendu parmi {valid_types}")
            errors += 1

        if mod.get("format") not in valid_formats:
            print(f"[ERREUR] [Module {mod_id}] Format invalide '{mod.get('format')}'. Attendu parmi {valid_formats}")
            errors += 1

    if errors == 0:
        print(f"[SUCCÈS] Le catalogue est 100% valide ({len(modules)} modules vérifiés).")
        return True
    else:
        print(f"[ÉCHEC] {errors} erreur(s) détectée(s) dans le catalogue.")
        return False

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cat = os.path.join(base_dir, "catalog.json")
    sch = os.path.join(base_dir, "schemas", "catalog.schema.json")
    success = validate_catalog(cat, sch)
    sys.exit(0 if success else 1)
