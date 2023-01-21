import flask
from cfg import models as models_list
from flask import jsonify, render_template, request
from utils import Predictions

models = models_list.models

app = flask.Flask(__name__)
app.config["debug"] = True


@app.route("/")
def home():
    # render landing page
    return render_template("index.html", models=models)


@app.route("/predict", methods=["POST"])
def predict_price():
    model_name = request.form.get("model_name")
    prev_date = request.form.get("prev_date")
    model = Predictions(model_name)
    pred = model.predict(prev_date)
    # render answer as JSON object
    return jsonify(
        {
            "Day": prev_date,
            "Predicted Price": list(pred["yhat"]),
        },
    )


if __name__ == "__main__":
    # host 0.0.0.0 for deployment using docker afterwards
    app.run(host="0.0.0.0", debug=True)