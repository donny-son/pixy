import base64

from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/save_image", methods=["POST"])
def save_image():
    try:
        data = request.get_json()
        if not data or "img_data" not in data:
            return "No image data received", 400
        img_data = data["img_data"]
        img_data = img_data.split(",")[1]
        img_bytes = base64.b64decode(img_data)
        filename = "drawing.png"
        with open(filename, "wb") as f:
            f.write(img_bytes)
        return "Image saved as {}".format(filename)
    except Exception as e:
        print("Error saving image:", e)
        return "Internal Server Error", 500


if __name__ == "__main__":
    app.run(debug=True)
