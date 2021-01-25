from flask import Flask, render_template, request, json

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/api', methods=['POST'])
def response():
    req = request.get_data()
    JSON = json.loads(req)

    return {
        "status": 200,
        "text": JSON['text'],
        "robot": JSON['robot']
    }


if __name__ == '__main__':
    app.run(port=8888, debug=True)
