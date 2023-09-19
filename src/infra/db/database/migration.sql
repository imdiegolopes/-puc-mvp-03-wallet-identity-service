-- Create a table named 'users' in the SQLite database

-- Note: SQLite databases are created automatically when you connect to them or open a database file.

-- Create a table named 'users'
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    created_on DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_on DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insert data into the 'users' table
INSERT INTO users (username, email, password)
VALUES
    ('diego', 'diego@fakemail.com', '078c007bd92ddec308ae2f5115c1775d');

