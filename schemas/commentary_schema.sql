-- =============================================================================
-- Open Shema — Standard SQLite Schema : Commentaires Bibliques
-- Format universel pour les commentaires verset par verset ou par section
-- =============================================================================

CREATE TABLE IF NOT EXISTS metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- Exemples de clés :
-- ('id', 'comm-calvin-evangiles')
-- ('author', 'Jean Calvin')
-- ('title', 'Commentaires sur la concordance ou harmonie évangélique')
-- ('year', '1555')
-- ('language', 'fr')

CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,            -- 1 à 66
    chapter_start INTEGER NOT NULL,
    verse_start INTEGER NOT NULL,
    chapter_end INTEGER,
    verse_end INTEGER,
    title TEXT,                          -- Titre de la péricope ou du thème
    content TEXT NOT NULL,               -- Contenu du commentaire (Markdown ou HTML nettoyé)
    order_index INTEGER DEFAULT 0
);

CREATE INDEX IF NOT EXISTS idx_comments_lookup ON comments(book_id, chapter_start, verse_start);
CREATE INDEX IF NOT EXISTS idx_comments_range ON comments(book_id, chapter_start, chapter_end);
