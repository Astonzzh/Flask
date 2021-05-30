from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("html.html")


@app.route('/_addNumbers')
def add_number():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a+b)


@app.route('/_mulNumbers')
def mul_number():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a*b)


@app.route('/static/txt.txt', methods=['POST'])
def load():
    return app.send_static_file("txt.txt")


if __name__ == '__main__':
    app.run()
