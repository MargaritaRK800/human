from flask import Flask, url_for, request, render_template
import json

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    param = dict()
    param['title'] = title
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    param = dict()
    param['title'] = prof
    return render_template('simulator.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')