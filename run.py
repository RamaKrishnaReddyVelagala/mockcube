from app import app
from markupsafe import escape

@app.route("/")
def welcome_message():
    return "Welcome to Flask Index Page."

@app.route("/user/<name>")
def welcome_user(name):
    return f"welcome special user {escape(name)}"

if __name__ == '__main__':
    app.run(debug=True)





# curl "localhost:5000/search?name=John&location=Miami"