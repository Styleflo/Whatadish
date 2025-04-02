from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['GET'])
def play():
    return render_template('play.html')

@app.route('/rule')
def rule():
    return render_template('rule.html')


if __name__ == '__main__':
    app.run(debug=True)