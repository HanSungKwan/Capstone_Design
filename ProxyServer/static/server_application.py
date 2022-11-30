import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    return "박인선 살빼자"


@app.route("/users/<user>/repos", methods=['GET', 'POST'])
def user_request(user):
    return f"hello,{user}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)