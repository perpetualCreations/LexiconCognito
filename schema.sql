DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS author;
DROP TABLE IF EXISTS publisher;
DROP TABLE IF EXISTS sourcedist;
DROP TABLE IF EXISTS tags;

CREATE TABLE author (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL PRIMARY KEY,
  notes TEXT
);

CREATE TABLE publisher (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  notes TEXT,
);

CREATE TABLE sourcedist ( -- This table is rather confusingly named, sourcedist refers to where the document was sourced from or distributed by
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  notes TEXT
):

CREATE TABLE tags (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT
);

CREATE TABLE item (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  authors TEXT, -- Numeric integer IDs of authors, separated with spaces
  date_digitalized TEXT NOT NULL, -- ISO8601 Format Dates, YYYY-MM-DD HH:MM:SS.SSS
  date_published TEXT, -- ISO8601 Format Dates, YYYY-MM-DD HH:MM:SS.SSS
  notes TEXT,
  publisher INTEGER,
  sourcedist INTEGER,
  tags TEXT, -- Tags separated with ', as a string, if document has a single tag, do not use any separators
  FOREIGN KEY(publisher) REFERENCES publisher(id),
  FOREIGN KEY(sourcedist) REFERENCES sourcedist(id)
);
