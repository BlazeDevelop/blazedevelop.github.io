from flask import Flask, render_template, request, redirect, url_for
from database import init_db, add_project, get_projects, get_project_by_id, delete_project
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Инициализация базы данных
init_db()

@app.route('/')
def index():
    # Здесь вы можете заменить данными о себе
    user_info = {
        'name': 'Владими',
        'surname': 'Буренко',
        'country': 'Казахстан',
        'programming_language': 'Python',
        'experience': '2 года',
        'links': 'https://github.com/BlazeDevelop'
    }
    return render_template('index.html', user_info=user_info)

@app.route('/projects')
def projects():
    projects = get_projects()
    return render_template('projects.html', projects=projects)

@app.route('/projects/<int:id>')
def project_detail(id):
    project = get_project_by_id(id)
    return render_template('project_detail.html', project=project)

@app.route('/add_project', methods=['POST'])
def add_new_project():
    title = request.form['title']
    description = request.form['description']
    languages = request.form['languages']
    image = request.files['image']
    image.save(f'static/uploads/{image.filename}')

    add_project(title, description, languages, f'uploads/{image.filename}')
    return redirect(url_for('projects'))

@app.route('/delete_project/<int:id>', methods=['POST'])
def delete_project_route(id):
    delete_project(id)
    return redirect(url_for('projects'))



if __name__ == '__main__':
    app.run(debug=True)
