# Données Open Shema — Structure des Répertoires

Ce dossier `data/` regroupe les bases de données binaires et fichiers de ressources libres de droits.

## Organisation

* **`bibles/`** : Fichiers SQLite ou JSON des versions bibliques (ex: `bible_lsg1910.sqlite`).
* **`dictionaries/`** : Fichiers SQLite de dictionnaires bibliques, lemmes et lexiques (ex: `dict_strong_fr.sqlite`).
* **`commentaries/`** : Fichiers SQLite de commentaires bibliques verset par verset (ex: `comm_calvin_evangiles.sqlite`).
* **`theology/`** : Ouvrages de théologie, traités, catéchismes et confessions de foi historiques (ex: `confession_rochelle_1559.sqlite`).

> ℹ️ Tous les fichiers présents dans ces sous-dossiers doivent être déclarés dans le fichier maître [catalog.json](../catalog.json) à la racine du dépôt.
