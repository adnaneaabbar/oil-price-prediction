import flask
from cfg import models as models_list
from flask import jsonify, render_template, request

models = models_list.models

app = flask.Flask(__name__)
app.config["debug"] = True


@app.route("/")
def home():
    # render landing page
    return render_template("index.html", models=models)


@app.route("/predict", methods=["POST"])
def predict_price():
    try:
        model_name = request.form.get("model_name")
        prev_date = request.form.get("date")
    except KeyError:
        # parse headers in request in case it's another client
        # other than browser where there is no form tag (curl..)
        model_name = request.headers.get("model_name")
        prev_date = request.headers.get("date")
    # render answer as JSON object
    return jsonify(
        {},
    )


if __name__ == "__main__":
    # host 0.0.0.0 for deployment using docker afterwards
    app.run(host="0.0.0.0", debug=True)