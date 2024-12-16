from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, current_user,login_user, logout_user, login_required

app = Flask(__name__, static_url_path="/static")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///coinDatabase.db"
app.config["SECRET_KEY"] = "marcRubin"

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)
    name = db.Column(db.String(30), nullable=False)

class Coin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    denomination = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer)
    condition = db.Column(db.String(20))

@login_manager.user_loader
def load_user(uid):
    user = User.query.get(uid)
    return user

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if user and password == user.password:
            login_user(user)
            return redirect("/")
        else:
            return render_template("login.html", message="failed to login, try again")
    return render_template("login.html", message="")


@app.route("/create", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        username = request.form['username']
        user = User(username=username, password=password, name=name)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect("/")
    return render_template("create.html")

@app.route("/piggybank", methods=['GET', 'POST'])
@login_required
def piggybank():
    print("test")
    if request.method == 'POST':
        print("postmode")
        #data = request.get_json(force=True)
        data = request.get_json(force=True)
        print("aaaaa")
        print(data)
        condition = data['condish']
        year = data['yr']
        denomination = data['denom']
        username= request.environ.get('username')
        print(username)
        user = User.query.filter_by(username=username).first()
        fk = user.id
        print(fk)
        coin = Coin(denomination=denomination, condition=condition, owner_id=fk, year=year)
        db.session.add(coin)
        db.session.commit()
        print("hello")
        return "yay"

    return render_template("piggybank.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("index.html")

@app.route("/funFact")
def funfact():
    return render_template("funFact.html")

"""
@app.route("/read")
@login_required
def read():
    prints = User.query.all()
    names = []
    #id=[]
    for i in prints:
        names.append(i)
    #for i in prints:
     #   names.append(i.name)
    return render_template("read.html", list = names)

"""

with app.app_context():
    db.create_all()

app.run(debug=True)