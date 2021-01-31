from flask import Flask, render_template, jsonify
from src.models import GitHubUserOrm, GitHubUser
from src.db import session

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "Hello, World!"


@app.route("/profiles", methods=["GET"])
def profiles():
    raw_users = session.query(GitHubUserOrm).all()
    users = [GitHubUser.from_orm(user).dict() for user in raw_users]
    return render_template("profiles.html", users=users)


@app.route("/api/profiles", methods=["GET"])
def api_profiles():
    raw_users = session.query(GitHubUserOrm).all()
    users = [GitHubUser.from_orm(user).dict() for user in raw_users]
    return jsonify(users)