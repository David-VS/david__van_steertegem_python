from flask import Flask, request

app = Flask(__name__)


@app.route('/binair')
def binair():
    value = int(request.args.get("dec"))
    if value > 64:
        return "te groot"
    else:
        return bin(value)


if __name__ == '__main__':
    app.run()
