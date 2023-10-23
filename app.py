from flask import Flask, render_template, request, jsonify
from ice_breaker import ice_break

app = Flask(__name__, template_folder="static/templates")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    person_info, profile_pic_url = ice_break(name)
    print(person_info)
    response = person_info.to_dict()
    response.update({"picture_url": profile_pic_url})
    return jsonify(response)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
