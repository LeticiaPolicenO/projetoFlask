from flask import Flask

app = Flask(__name__)
app.config['HOST'] = '127.0.0.1'
app.config['PORT']=8000
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False