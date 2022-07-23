from flask import Flask, render_template
from heroku import NAME,IMAGE, SHORT_BIO, ABOUT, GITHUB, SNAPCHAT, TELEGRAM, INSTAGRAM

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name=NAME, image=IMAGE, bio=SHORT_BIO, about=ABOUT, git=GITHUB, sc=SNAPCHAT, tg=TELEGRAM, ig=INSTAGRAM)



if __name__ == "__main__":
    app.run(debug=False)
