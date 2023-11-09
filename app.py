from flask import Flask, request
app = Flask(__name__)

db_users = {"victor":"paris",
            "john":"london",}

@app.route('/')
def hello_world():
    return 'Hello, Welcome to your Base Application!'

@app.route('/greet')
def greet_user():
    return 'Hello Victor, this is Docker! Greet method'

@app.route('/dbusers')
def get_db_users():
    "gets users by id or all users by default eg; /dbusers?name=victor"
    suppplied_args = request.args
    user = suppplied_args.get('user',default="all")
    if user == "all":
        return db_users
    return {"user":user,"location":db_users[user]} if user in db_users.keys()  else "User not found"