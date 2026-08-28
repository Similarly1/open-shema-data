-- =============================================================================
-- Open Shema — Standard SQLite Schema : Dictionnaires & Lexiques
-- Format universel pour dictionnaires Strong, Bailly, Gesenius, Thayer, etc.
-- =============================================================================

CREATE TABLE IF NOT EXISTS metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- Exemples de clés requises :
-- ('id', 'dict-strong-fr')
-- ('title', 'Dictionnaire Strong Hébreu & Grec')
-- ('language', 'fr')
-- ('type', 'strong_lexicon')

CREATE TABLE IF NOT EXISTS entries (
    id TEXT PRIMARY KEY,              -- Ex: 'H7225', 'G0025', 'grace', 'alliance'
    language TEXT NOT NULL,           -- 'hebrew', 'greek', 'latin', 'french'
    lemma TEXT,                       -- Mot original (ex: 'רֵאשִׁית', 'ἀγάπη')
    transliteration TEXT,             -- Prononciation/phonétique (ex: 'reishiyth', 'agape')
    pronunciation_guide TEXT,         -- Guide audio ou transcription API
    derivation TEXT,                  -- Étymologie / racine d'origine
    part_of_speech TEXT,              -- 'nom féminin', 'verbe', etc.
    definition TEXT NOT NULL,         -- Définition complète (supporte HTML/Markdown)
    short_definition TEXT,            -- Résumé court (1 phrase)
    kjv_def TEXT                      -- Traductions courantes / équivalents
);

CREATE INDEX IF NOT EXISTS idx_entries_lemma ON entries(lemma);
CREATE INDEX IF NOT EXISTS idx_entries_translit ON entries(transliteration);
