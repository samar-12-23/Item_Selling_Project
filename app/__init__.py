from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///item_feature.db'
app.config['SECRET_KEY']= 'e8c7e803482f4b90d81568a5'

bcrypt=Bcrypt(app)
db=SQLAlchemy(app)
login_manager=LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'



from app import routes



# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/samar")
# def samar():
#     return "<p>Hello, Samar!</p>"

# @app.route('/about/<username>')
# def about(username):
#     return f'<h1>This is the about page of {username}</h1>'
app.run(debug=True)     
with app.app_context():
    db.create_all()
