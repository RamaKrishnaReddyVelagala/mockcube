from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def welcome_message():
    return "Welcome to Flask Index Page."

@app.route("/user:<name>")
def welcome_user(name):
    return f"welcome special user {escape(name)}"

@app.route("/search", methods=['GET'])
def search_user():
    args = request.args
    # print(args.to_dict())
    print(args.get("name"))
    print(args.get("location"))
    return args

if __name__ == "__main__":
    app.run(debug=True)