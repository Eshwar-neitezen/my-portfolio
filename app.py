import json
from flask import Flask, render_template
from flask_frozen import Freezer
from collections import defaultdict

# --- CONFIGURATION ---
ALL_CATEGORIES = ["Robotics", "ECE Topics", "Music Theory", "Astrophysics"]

# --- APP SETUP ---
app = Flask(__name__)
app.config["DEBUG"] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True # Helps with some deployment environments
freezer = Freezer(app) # This is the line that was missing from your GitHub version

# --- HELPER FUNCTIONS ---
def load_projects():
    try:
        with open('content/projects.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def load_posts():
    try:
        with open('content/blog.json', 'r', encoding='utf-8') as f:
            return sorted(json.load(f), key=lambda x: x['date'], reverse=True)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# --- ROUTES ---
@app.route('/')
def index():
    all_posts = load_posts()
    all_projects = load_projects()
    featured_projects = [p for p in all_projects if p.get("featured", False)]
    return render_template('index.html', posts=all_posts[:3], projects=featured_projects)

@app.route('/projects.html')
def projects():
    all_projects = load_projects()
    return render_template('projects.html', projects=all_projects)

@app.route('/blog.html')
def blog():
    posts = load_posts()
    grouped_posts = defaultdict(list)
    for post in posts:
        grouped_posts[post['category']].append(post)
    return render_template('blog.html', all_categories=ALL_CATEGORIES, grouped_posts=grouped_posts)

@app.route('/notes.html')
def notes():
    return render_template('notes.html')

# --- MAIN ---
if __name__ == '__main__':
   
    app.run(debug=True, port=8000)