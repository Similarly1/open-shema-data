# Open Shema — Data Hub 📖⚡

[![Catalog Validation](https://github.com/Similarly1/open-shema-data/actions/workflows/validate_catalog.yml/badge.svg)](https://github.com/Similarly1/open-shema-data/actions/workflows/validate_catalog.yml)
[![License: CC0 / Public Domain](https://img.shields.io/badge/License-Public%20Domain-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

Dépôt officiel des ressources textuelles, bases de données, lexiques, commentaires et jeux de données libres de droits pour l'écosystème **Open Shema** et toute application d'étude biblique ouverte.

---

## 🎯 Objectifs

1. **Gratuité & Liberté totale** : Fournir des textes bibliques, dictionnaires hébreu/grec et ouvrages de théologie historiques sous licences libres ou domaine public.
2. **Installation en 1 clic** : Permettre aux applications clientes d'interroger un catalogue dynamique (`catalog.json`) sans mise à jour logicielle nécessaire.
3. **Haute Performance** : Formats standardisés (SQLite optimisé avec index et JSON structuré) pour des recherches instantanées, y compris hors-ligne.

---

## 📁 Architecture du Dépôt

```text
open-shema-data/
├── catalog.json                     # 🌟 Fichier maître recensant tous les modules disponibles
├── bibleproject_fr.json             # Dataset des vidéos de panoramas et affiches HD (BibleProject FR)
│
├── schemas/                         # 📐 Schémas SQL et JSON officiels
│   ├── catalog.schema.json          # Schéma JSON formel de validation
│   ├── bible_schema.sql             # Schéma SQLite pour textes bibliques & strongs
│   ├── dictionary_schema.sql        # Schéma SQLite pour dictionnaires & racines
│   ├── commentary_schema.sql        # Schéma SQLite pour commentaires verset par verset
│   └── theology_schema.sql          # Schéma SQLite pour traités & confessions de foi
│
├── data/                            # 📦 Données binaires prêtes au téléchargement
│   ├── bibles/                      # Traductions (ex: bible_lsg1910.sqlite)
│   ├── dictionaries/                # Lexiques (ex: dict_strong_fr.sqlite)
│   ├── commentaries/                # Commentaires (ex: comm_calvin_evangiles.sqlite)
│   └── theology/                    # Ouvrages théologiques (ex: confession_rochelle_1559.sqlite)
│
├── scripts/                         # 🛠️ Scripts d'automatisation & validation
│   ├── validate_catalog.py          # Validation de l'intégrité du catalogue
│   └── update_data.py               # Synchronisation automatique YouTube / BibleProject
│
└── .github/workflows/               # 🤖 CI/CD automatisé
    ├── validate_catalog.yml         # Validation du catalogue à chaque PR / Push
    └── update_bibleproject_data.yml # Synchronisation hebdomadaire BibleProject
```

---

## 🚀 Utilisation dans une Application (Client)

### 1. URL du Catalogue
Toute application (Web, Desktop, Mobile) peut récupérer le catalogue via GitHub Raw ou via CDN rapide :
* **GitHub Raw** : `https://raw.githubusercontent.com/Similarly1/open-shema-data/main/catalog.json`
* **jsDelivr CDN (Cache mondial)** : `https://cdn.jsdelivr.net/gh/Similarly1/open-shema-data@main/catalog.json`

### 2. Exemple d'Intégration (TypeScript / JavaScript)

```typescript
// Récupération des modules disponibles
async function loadAvailableModules() {
  const response = await fetch('https://raw.githubusercontent.com/Similarly1/open-shema-data/main/catalog.json');
  const catalog = await response.json();
  
  console.log(`Modules disponibles : ${catalog.modules.length}`);
  catalog.modules.forEach(mod => {
    console.log(`[${mod.type.toUpperCase()}] ${mod.title} (${mod.language}) -> ${mod.download_url}`);
  });
}
```

---

## 📖 Schémas de Données

Tous les modules respectent des schémas stricts afin d'assurer l'interopérabilité directe :

* **Bibles** : Tables `metadata`, `books`, `verses` (avec colonnes `text` et `text_strong`).
* **Dictionnaires** : Tables `metadata`, `entries` (`lemma`, `transliteration`, `definition`, `kjv_def`).
* **Commentaires** : Tables `metadata`, `comments` (`book_id`, `chapter_start`, `verse_start`, `content`).
* **Théologie** : Tables `metadata`, `chapters`, `sections` (`title`, `content`, `scripture_proofs`).

Consultez le dossier [`schemas/`](schemas/) pour les définitions SQL complètes.

---

## 🤝 Comment Contribuer ?

Vous souhaitez ajouter un livre théologique, une traduction libre ou un dictionnaire ?

1. Assurez-vous que l'ouvrage est strictement dans le **domaine public** ou sous une **licence ouverte (CC-BY, CC0)**.
2. Structurez la base selon le schéma SQL adéquat dans [`schemas/`](schemas/).
3. Placez le fichier dans le dossier correspondant sous `data/`.
4. Ajoutez la fiche du module dans `catalog.json`.
5. Lancez la validation locale :
   ```bash
   python scripts/validate_catalog.py
   ```
6. Ouvrez une **Pull Request**.

---

## 📜 Licence

Les données compilées dans ce dépôt sont publiées sous **Domaine Public / CC0**, sauf mention contraire spécifique stipulée dans les métadonnées de chaque module (ex. vidéos BibleProject protégées par les droits de leurs créateurs respectifs).
