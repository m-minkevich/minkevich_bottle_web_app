import sqlite3

conn = sqlite3.connect('projects.db') # The file is going to be created in this directory

# conn.execute("CREATE TABLE projects (id INTEGER PRIMARY KEY, name char(100) NOT NULL, author char(100) NOT NULL)")
conn.execute("INSERT INTO projects (name, author) VALUES ('new project', 'Me')")
conn.commit()