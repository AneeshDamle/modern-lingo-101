# Modern Lingo Learner

from flask import Flask, render_template, request

app = Flask(__name__)


LINGOS = [
    "GG",
    "LEGIT",
    "RIZZZ",
    "POGCHAMP"

]

@app.route("/")
def index():
    return render_template("index.html", lingos=LINGOS)

@app.route("/lingo", methods=["POST"])

def register():
  
  # Validate request
  if request.form.get("lingo") not in LINGOS:
      return render_template("failure.html")
  
  if (request.form.get("lingo") == "LEGIT"):
      return render_template("legit.html")
  
  if (request.form.get("lingo") == "GG HOGAYA"):
      return render_template("gg_hogaya.html")
  
  if (request.form.get("lingo") == "RIZZZ"):
      return render_template("rizzz.html")
  
  if (request.form.get("lingo") == "POGCHAMP"):
      return render_template("pogchamp.html")



