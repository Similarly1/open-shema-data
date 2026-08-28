-- =============================================================================
-- Open Shema — Standard SQLite Schema : Ouvrages Théologiques & Confessions
-- Format universel pour traités, confessions de foi, catéchismes, écrits patristiques
-- =============================================================================

CREATE TABLE IF NOT EXISTS metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- Exemples de clés :
-- ('id', 'theology-confession-rochelle')
-- ('title', 'Confession de foi de La Rochelle')
-- ('author', 'Jean Calvin / Synode')
-- ('type', 'confession_of_faith')

CREATE TABLE IF NOT EXISTS chapters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_index INTEGER NOT NULL,
    title TEXT NOT NULL,
    subtitle TEXT
);

CREATE TABLE IF NOT EXISTS sections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter_id INTEGER,
    order_index INTEGER NOT NULL,
    section_number TEXT,                 -- 'Article 1', 'Question 25', etc.
    title TEXT,
    content TEXT NOT NULL,               -- Texte complet (Markdown ou HTML)
    scripture_proofs TEXT,               -- Références bibliques associées (JSON array ou texte)
    FOREIGN KEY (chapter_id) REFERENCES chapters(id)
);

CREATE INDEX IF NOT EXISTS idx_theology_order ON sections(chapter_id, order_index);
