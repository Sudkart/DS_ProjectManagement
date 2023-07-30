from platform import java_ver
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index1():
    if request.method == "POST":
        tweet = request.form["tweet"]
        cleaned_tweet = re.sub(r"(@[A-Za-z0-9_]+)|[^\w\s\n]|#|http\S+", "", tweet.lower())
        prediction = Nb_Model.predict([cleaned_tweet])[0]

        return render_template("index1.html", prediction=prediction)

    return render_template("index1.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)