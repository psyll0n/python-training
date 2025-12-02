# Frameworks

Web application frameworks and their implementations. This section covers popular Python web frameworks for building web applications.

## 📂 Contents

### [Django](./frameworks/django/)
High-level Python web framework that encourages rapid development and clean, pragmatic design.

**Django Philosophy:**
- "Batteries included" - comes with many features built-in
- DRY (Don't Repeat Yourself) principle
- MVC/MVT architecture (Model-View-Template)
- Strong ORM (Object-Relational Mapping)
- Built-in admin interface

**Core Components:**
- **Models** - Database structure
- **Views** - Business logic
- **Templates** - HTML presentation
- **URLs** - Route mapping
- **Forms** - Input handling
- **Admin** - Automatic admin interface

**Common Django Commands:**
```bash
# Create new project
django-admin startproject myproject

# Create new app
python manage.py startapp myapp

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

**Django Project Structure:**
```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py    # Configuration
│   ├── urls.py        # URL routing
│   ├── wsgi.py        # WSGI config
│   └── asgi.py        # ASGI config
└── myapp/
    ├── __init__.py
    ├── models.py      # Database models
    ├── views.py       # View functions/classes
    ├── urls.py        # App URL routing
    ├── admin.py       # Admin interface
    ├── forms.py       # Form classes
    ├── tests.py       # Unit tests
    └── templates/     # HTML templates
```

**Example Model:**
```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
```

**Example View:**
```python
from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {
        'articles': articles
    })
```

**When to Use Django:**
- Large, complex web applications
- Need built-in features (auth, admin, ORM)
- Database-driven applications
- Need rapid development
- Enterprise applications

**Best For:**
- Content management systems
- E-commerce platforms
- Social networks
- Data-driven websites
- RESTful APIs (with Django REST framework)

---

### [Flask](./frameworks/flask/)
Lightweight WSGI web application framework - micro-framework for Python.

**Flask Philosophy:**
- Minimalist and flexible
- "Micro" doesn't mean less capable
- Provides the basics, you add what you need
- Extensible through plugins
- Simple and explicit

**Core Components:**
- **Routes** - URL mapping with decorators
- **Views** - Function-based views
- **Templates** - Jinja2 templating
- **Request/Response** - HTTP handling
- **Sessions** - User session management

**Basic Flask App:**
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}!'

@app.route('/api/data', methods=['POST'])
def handle_data():
    data = request.json
    return {'status': 'success'}

if __name__ == '__main__':
    app.run(debug=True)
```

**Flask Project Structure:**
```
myflaskapp/
├── app.py              # Main application
├── config.py           # Configuration
├── requirements.txt    # Dependencies
├── static/             # CSS, JS, images
│   ├── css/
│   ├── js/
│   └── images/
├── templates/          # HTML templates
│   ├── base.html
│   ├── index.html
│   └── about.html
└── models.py           # Database models (optional)
```

**Popular Flask Extensions:**
- **Flask-SQLAlchemy** - Database ORM
- **Flask-Login** - User authentication
- **Flask-WTF** - Forms and validation
- **Flask-Mail** - Email support
- **Flask-RESTful** - REST API building
- **Flask-Admin** - Admin interface
- **Flask-Migrate** - Database migrations

**Example with SQLAlchemy:**
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
```

**When to Use Flask:**
- Small to medium applications
- Need flexibility and control
- Microservices architecture
- RESTful APIs
- Prototypes and MVPs

**Best For:**
- REST APIs
- Single-page applications (SPA backends)
- Microservices
- Quick prototypes
- Simple web applications

---

## 🆚 Django vs Flask Comparison

| Feature | Django | Flask |
|---------|--------|-------|
| **Type** | Full-stack framework | Micro-framework |
| **Philosophy** | Batteries included | Minimalist |
| **Learning Curve** | Steeper | Gentler |
| **Database** | Built-in ORM | Need extension |
| **Admin Interface** | Built-in | Need extension |
| **Template Engine** | Django templates | Jinja2 |
| **Forms** | Built-in | Need extension |
| **Auth** | Built-in | Need extension |
| **URL Routing** | URLs file | Decorators |
| **Flexibility** | Opinionated | Very flexible |
| **Best For** | Large apps | Small-medium apps |
| **Project Structure** | Structured | Flexible |

## 🎯 Learning Path

### Django Path
1. **Setup** - Install Django, create project
2. **Models** - Define database structure
3. **Admin** - Use built-in admin interface
4. **Views & URLs** - Create pages and routes
5. **Templates** - Build HTML interfaces
6. **Forms** - Handle user input
7. **Authentication** - User login/logout
8. **Deployment** - Deploy to production

### Flask Path
1. **Setup** - Install Flask, create app
2. **Routes** - Define URL patterns
3. **Templates** - Create Jinja2 templates
4. **Forms** - Add WTForms extension
5. **Database** - Integrate SQLAlchemy
6. **Authentication** - Add Flask-Login
7. **API** - Build RESTful endpoints
8. **Deployment** - Deploy to production

## 💡 Best Practices

### Django Best Practices
```python
# Use class-based views for complex logic
from django.views.generic import ListView

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'
    context_object_name = 'articles'

# Use Django's built-in features
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')

# Use environment variables for secrets
import os
SECRET_KEY = os.environ.get('SECRET_KEY')
```

### Flask Best Practices
```python
# Use application factory pattern
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    login_manager.init_app(app)
    
    return app

# Use blueprints for organization
from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/users')
def get_users():
    return jsonify(users)

app.register_blueprint(api)

# Use config objects
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
```

## 🚀 Deployment

### Django Deployment Checklist
- Set DEBUG = False
- Configure ALLOWED_HOSTS
- Use environment variables for secrets
- Set up static files (collectstatic)
- Configure database (PostgreSQL)
- Use gunicorn/uwsgi
- Set up reverse proxy (nginx)
- Enable HTTPS

### Flask Deployment Checklist
- Set debug mode to False
- Use production WSGI server (gunicorn)
- Configure reverse proxy (nginx)
- Set environment variables
- Use production database
- Enable logging
- Set up HTTPS
- Configure static files

## 📚 Resources

### Django
- Official Documentation: docs.djangoproject.com
- Django REST Framework
- Django Channels (WebSockets)
- Third-party packages: djangopackages.org

### Flask
- Official Documentation: flask.palletsprojects.com
- Flask Mega-Tutorial by Miguel Grinberg
- Flask extensions: flask.palletsprojects.com/extensions
- Awesome Flask: github.com/humiaozuzu/awesome-flask

## 🔧 Common Tasks

### Database Operations
```python
# Django
from myapp.models import Article
articles = Article.objects.all()
article = Article.objects.get(id=1)
Article.objects.create(title='New', content='...')

# Flask (with SQLAlchemy)
from models import Article
articles = Article.query.all()
article = Article.query.get(1)
db.session.add(Article(title='New', content='...'))
db.session.commit()
```

### Forms
```python
# Django
from django.forms import ModelForm

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

# Flask (with WTForms)
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField

class ArticleForm(FlaskForm):
    title = StringField('Title')
    content = TextAreaField('Content')
```
