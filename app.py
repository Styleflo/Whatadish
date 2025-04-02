from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        user_answer = request.form.get('answer')
    return render_template('play.html')

@app.route('/rule')
def rule():
    return render_template('rule.html')


if __name__ == '__main__':
    app.run(debug=True)