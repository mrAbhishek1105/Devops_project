from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/about')
def about():
    return '<h1>This Page and this site is created by me(Abhishek kumar KK)</h1>'

if __name__ == '--main--':
    app.run(debug=True, port=5000)
    