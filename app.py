from dataManager import *
from flask import Flask, render_template, request
from proximity import proximity_percentage

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

data = ""
@app.route('/play', methods=['GET', 'POST'])
def play():
    global data
    if request.method == 'GET':
        data = pickNewData()

    if request.method == 'POST':
        user_answer = request.form.get('answer')
        if verifyAnswer(user_answer, data['Origine(pays)']):
            if isEndOfData():
                pass
                #redirect
            else:
                data = pickNewData()
        else:
            percentage = proximity_percentage(user_answer, data['Origine(pays)'])

    return render_template('play.html', dish_name= data['Nom'], image_path=f"images/plats/{data['Photo']}")

@app.route('/rule')
def rule():
    return render_template('rule.html')


if __name__ == '__main__':
    app.run(debug=True)