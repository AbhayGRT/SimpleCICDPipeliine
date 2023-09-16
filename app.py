from flask import Flask, render_template, request
import instaloader

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        profile = request.form["profile"]

        # Create an Instaloader instance
        loader = instaloader.Instaloader()

        # Download the profile's images, videos, and captions
        loader.download_profile(profile)

        # Return a successful message of completion
        return render_template("success.html")

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)
