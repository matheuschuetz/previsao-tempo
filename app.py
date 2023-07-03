from flask import Flask
from flask import render_template
from flask import request
import requests

app = Flask(__name__)
app.debug = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city_name = request.form["nome_cidade"]
        response = requests.get(f"https://api.hgbrasil.com/weather?key=SUA-CHAVE&city_name={city_name}")
        result = response.json()
        if result["results"]["condition_slug"] == "storm":
            image_filename =  "snow.png"
        elif result["results"]["condition_slug"] == "rain":
            image_filename = "rain.png"
        elif result["results"]["condition_slug"] == "fog":
            image_filename = "mist.png"
        elif result["results"]["condition_slug"] == "clear_day":
            image_filename = "clear.png"
        elif result["results"]["condition_slug"] == "cloud":
            image_filename = "cloud.png"
        elif result["results"]["currently"] == "noite":
            image_filename = "night.png"
        else:
            image_filename =  "cloud.png"
        image_path = f"static/images/{image_filename}"
        return render_template("index.html", result=result, image_path=image_path)
    return render_template("index.html")


if __name__ == "__main__":
    app.run()

