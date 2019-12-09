from flask import Flask, jsonify
from ludwig.api import LudwigModel
import pandas

app = Flask(__name__)

model = LudwigModel.load("model")

@app.route("/predict", methods=["POST"])
def predict(request):
    json = request.get_json()

    extract = json.get("extract", None)
    if extract is None:
        return "extract is required"

    prediction = model.predict(data_df=getDataFrame(extract), return_type="dict")["film"]
    return jsonify({
        "class": prediction['predictions'][0],
        "probability": str(prediction['probability'][0])
    })

def getDataFrame(extract):
    return pandas.DataFrame({
        "extract": [extract]
    })

if __name__ == '__main__':
    app.run(port=3000)
