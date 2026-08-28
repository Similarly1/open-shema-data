-- =============================================================================
-- Open Shema — Standard SQLite Schema : Bibles
-- Format universel pour les traductions et manuscrits bibliques
-- =============================================================================

-- Table des métadonnées de la version
CREATE TABLE IF NOT EXISTS metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- Exemples de clés requises :
-- ('id', 'lsg-1910')
-- ('title', 'Louis Segond 1910')
-- ('language', 'fr')
-- ('has_strong', '1')
-- ('has_notes', '0')
-- ('license', 'Public Domain')

-- Table ordonnée des 66 livres (ou deutérocanoniques si spécifié)
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,           -- 1 = Genèse ... 39 = Malachie, 40 = Matthieu ... 66 = Apocalypse
    testament TEXT NOT NULL CHECK (testament IN ('OT', 'NT', 'APO', 'DC')),
    code TEXT NOT NULL UNIQUE,        -- Code standard à 3 lettres : GEN, EXO, MAT, REV...
    name TEXT NOT NULL,               -- 'Genèse', 'Exode', 'Matthieu'...
    short_name TEXT NOT NULL,         -- 'Gen', 'Ex', 'Mt'...
    chapters_count INTEGER NOT NULL,  -- Nombre total de chapitres
    order_index INTEGER NOT NULL      -- Ordre d'affichage
);

-- Table des versets
CREATE TABLE IF NOT EXISTS verses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    chapter INTEGER NOT NULL,
    verse INTEGER NOT NULL,
    text TEXT NOT NULL,               -- Texte pur lisible
    text_strong TEXT,                 -- Texte enrichi avec balises de lemmes : ex. "Au commencement<H7225>..."
    notes TEXT,                       -- Notes de bas de page (format JSON ou HTML)
    FOREIGN KEY (book_id) REFERENCES books(id)
);

-- Index de performance critiques
CREATE INDEX IF NOT EXISTS idx_verses_bcv ON verses(book_id, chapter, verse);
CREATE INDEX IF NOT EXISTS idx_verses_lookup ON verses(book_id, chapter);
