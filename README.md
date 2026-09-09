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
│   ├── update_readme_catalog.py     # Synchronisation automatique du README avec catalog.json
│   └── update_data.py               # Synchronisation automatique YouTube / BibleProject
│
└── .github/workflows/               # 🤖 CI/CD automatisé
    ├── validate_catalog.yml         # Validation du catalogue à chaque PR / Push
    └── update_bibleproject_data.yml # Synchronisation hebdomadaire BibleProject
```

---

<!-- START_CATALOG -->

## 📚 Ouvrages & Ressources Disponibles

> 💡 Le catalogue compte actuellement **10 modules** prêts au téléchargement direct ou via l'API client.

### 📖 Traductions Bibliques

Traductions intégrales de l'Ancien et du Nouveau Testament avec indexation textuelle et codes Strong.

| Couverture | Module | Code | Auteur / Éditeur | Format & Taille | Licence | Téléchargement |
| :---: | :--- | :---: | :--- | :---: | :---: | :---: |
| <img src="https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/covers/LSG.png" width="42" alt="LSG"> | **Louis Segond 1910 (avec Strongs)** | `LSG` | Louis Segond | SQLITE (20.1 Mo) | Public Domain | [⬇️ Télécharger](https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/bibles/bible_lsg1910.sqlite) |
| <img src="https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/covers/DARBY.png" width="42" alt="DARBY"> | **Bible J.N. Darby (avec Strong)** | `DARBY` | John Nelson Darby | SQLITE (21.3 Mo) | Public Domain | [⬇️ Télécharger](https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/bibles/bible_darby.sqlite) |
| <img src="https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/covers/OST.png" width="42" alt="OST"> | **Bible Ostervald** | `OST` | Jean-Frédéric Ostervald (Éd. La Maison de la Bible) | SQLITE (5.5 Mo) | Public Domain | [⬇️ Télécharger](https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/bibles/bible_ostervald.sqlite) |
| <img src="https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/covers/STAPFER.png" width="42" alt="STAPFER"> | **Le Nouveau Testament (Traduction Edmond Stapfer)** | `STAPFER` | Edmond Stapfer (Librairie Fischbacher) | SQLITE (1.4 Mo) | Public Domain | [⬇️ Télécharger](https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/bibles/bible_stapfer.sqlite) |
| <img src="https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/covers/GIG.png" width="42" alt="GIG"> | **La Sainte Bible d'après les Septante** | `GIG` | Pierre Giguet / Lethielleux | SQLITE (4.0 Mo) | Public Domain | [⬇️ Télécharger](https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/bibles/bible_septante_giguet.sqlite) |
| <img src="https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/covers/NCL.png" width="42" alt="NCL"> | **Sainte Bible néo-Crampon Libre** | `NCL` | Augustin Crampon (Révision Fraternité de Tibériade) | SQLITE (6.3 Mo) | Creative Commons (CC-BY-SA 4.0) | [⬇️ Télécharger](https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/bibles/bible_ncl.sqlite) |

### 💬 Commentaires Bibliques

Commentaires verset par verset et analyses exégétiques structurées.

| Couverture | Module | Code | Auteur / Éditeur | Format & Taille | Licence | Téléchargement |
| :---: | :--- | :---: | :--- | :---: | :---: | :---: |
| <img src="https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/covers/CBJC.png" width="42" alt="CBJC"> | **Commentaire Biblique de Jean Calvin** | `CBJC` | Jean Calvin (Éd. Ch. Meyrueis / Dom. Public) | SQLITE (36.8 Mo) | Public Domain | [⬇️ Télécharger](https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/commentaires/comm_calvin.sqlite) |

### 🏛️ Théologie & Dogmatique

Traités doctrinaux majeurs, théologies systématiques et confessions de foi historiques.

| Couverture | Module | Code | Auteur / Éditeur | Format & Taille | Licence | Téléchargement |
| :---: | :--- | :---: | :--- | :---: | :---: | :---: |
| <img src="https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/covers/HODGE.png" width="42" alt="HODGE"> | **Théologie Systématique (3 volumes)** | `HODGE` | Charles Hodge (Séminaire de Princeton, 1871–1873) | SQLITE (14.8 Mo) | Public Domain (Traduction Moderne Open Shema) | [⬇️ Télécharger](https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/theology/theologie_systematique_hodge.sqlite) |

### 📚 Dictionnaires & Encyclopédies

Lexiques originaux, dictionnaires bibliques encyclopédiques et définitions théologiques.

| Couverture | Module | Code | Auteur / Éditeur | Format & Taille | Licence | Téléchargement |
| :---: | :--- | :---: | :--- | :---: | :---: | :---: |
| <img src="https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/covers/VIGOUROUX.png" width="42" alt="VIGOUROUX"> | **Dictionnaire de la Bible (F. Vigouroux)** | `VIGOUROUX` | Fulgrence Vigouroux & Collaborateurs (1895–1912) | JSON (34.6 Mo) | Public Domain | [⬇️ Télécharger](https://raw.githubusercontent.com/Similarly1/open-shema-data/main/data/dictionaries/vigouroux_dict.json) |

### 🎨 Jeux de Données & Multimédia

Données multimédias, liens vidéos, affiches HD et métadonnées complémentaires.

| Couverture | Module | Code | Auteur / Éditeur | Format & Taille | Licence | Téléchargement |
| :---: | :--- | :---: | :--- | :---: | :---: | :---: |
| — | **BibleProject Français (Panoramas & Affiches)** | `BP-FR` | BibleProject | JSON (81 Ko) | Creative Commons / BibleProject | [⬇️ Télécharger](https://raw.githubusercontent.com/Similarly1/open-shema-data/main/bibleproject_fr.json) |

<!-- END_CATALOG -->

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

## 🔒 Maintenance & Gouvernance

Ce dépôt est exclusivement administré et alimenté par l'équipe **Open Shema**. Les ressources, traductions et ouvrages intégrés sont rigoureusement vérifiés, structurés et indexés par le mainteneur officiel avant publication dans le catalogue.

---

## 📜 Licence

Les données compilées dans ce dépôt sont publiées sous **Domaine Public / CC0**, sauf mention contraire spécifique stipulée dans les métadonnées de chaque module (ex. vidéos BibleProject protégées par les droits de leurs créateurs respectifs).
