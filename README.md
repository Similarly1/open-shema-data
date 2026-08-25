# Open Shema — Data Hub 📖

Dépôt officiel des données documentaires, multimédias, dictionnaires, cartes et indexations théologiques pour l'écosystème **Open Shema**.

---

## Contenu du Répertoire

* **`bibleproject_fr.json`** : Cartographie exhaustive des 66 livres bibliques avec vidéos de panorama officielles en français (Playlists YouTube de la chaîne *BibleProject - Français*) et affiches littéraires haute définition (CDN CloudFront).
* **`.github/workflows/update_bibleproject_data.yml`** : Workflow automatisé (GitHub Actions) exécuté chaque dimanche à minuit UTC pour détecter et indexer automatiquement les nouvelles vidéos et ressources.
* **`scripts/update_data.py`** : Script Python autonome d'extraction et de synchronisation via `yt-dlp`.

---

## Synchronisation Automatique

Ce dépôt est mis à jour chaque semaine par un robot GitHub Action. Les applications clientes Open Shema interrogent ce dépôt pour recevoir automatiquement les dernières péricopes et contenus sans nécessiter de mise à jour de l'application logicielle.
