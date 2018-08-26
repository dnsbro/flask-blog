from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

db.create_all()

@app.route('/')
def index():
    username = ''   #需要获取到前端的用户名
    password = ''   #密码
    user = User.query.filter(User.username == username).first();
    if user != None and password == user.password:
        return render_template('login.html')
    else:
        render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
