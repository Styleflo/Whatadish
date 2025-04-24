from helper.dataManager import *
from flask import Flask, render_template, request

app = Flask(__name__)

data = ""
compteur = 1
score = 0
reponses = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['GET', 'POST'])
def play():

    global data
    global compteur
    global score
    global reponses

    if request.method == 'GET':
        data = pickNewData()

    if request.method == 'POST':
        user_answer = request.form.get('answer')

        if not isCountry(user_answer):
            return render_template('play.html', score=score, previous_guesses=reponses, dish_name=data['Nom'], image_path=f"images/plats/{data['Photo']}", message="Wrong spelling")

        percentage = proximity_percentage(user_answer, data['Origine(pays)'])
        reponses.append((percentage, user_answer))
        reponses.sort(key=lambda x: x[0], reverse=True)

        if verifyAnswer(user_answer, data['Origine(pays)']):
            score = score + int(100 / len(reponses))
            reponses = []
            if isEndOfData():
                pass
            else:
                data = pickNewData()
        else:
            pass
    return render_template('play.html', score=score, previous_guesses=reponses, dish_name= data['Nom'], image_path=f"images/plats/{data['Photo']}", message="Entrez un pays")

@app.route('/rule')
def rule():
    return render_template('rule.html')


if __name__ == '__main__':
    app.run(debug=True)