import sqlite3

def init_db():
    conn = sqlite3.connect('portfolio.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS projects
                 (id INTEGER PRIMARY KEY,
                 title TEXT,
                 description TEXT,
                 languages TEXT,
                 image TEXT)''')

    conn.commit()
    conn.close()

def add_project(title, description, languages, image):
    conn = sqlite3.connect('portfolio.db')
    c = conn.cursor()

    c.execute("INSERT INTO projects (title, description, languages, image) VALUES (?, ?, ?, ?)",
              (title, description, languages, image))

    conn.commit()
    conn.close()

def get_projects():
    conn = sqlite3.connect('portfolio.db')
    c = conn.cursor()

    c.execute("SELECT * FROM projects")
    projects = c.fetchall()

    conn.close()

    return projects

def get_project_by_id(id):
    conn = sqlite3.connect('portfolio.db')
    c = conn.cursor()

    c.execute("SELECT * FROM projects WHERE id=?", (id,))
    project = c.fetchone()

    conn.close()

    return project

def delete_project(id):
    conn = sqlite3.connect('portfolio.db')
    c = conn.cursor()

    c.execute("DELETE FROM projects WHERE id=?", (id,))

    conn.commit()
    conn.close()