from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load Model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    year = int(data["year"])
    present_price = float(data["present_price"])
    kms = float(data["kms_driven"])
    fuel = int(data["fuel_type"])
    seller = int(data["seller_type"])
    trans = int(data["transmission"])
    owner = int(data["owner"])

    arr = np.array([[year, present_price, kms, fuel, seller, trans, owner]])

    output = model.predict(arr)[0]

    return jsonify({"price": round(output, 2)})

if __name__ == "__main__":
    app.run(debug=True)
