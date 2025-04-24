from helper.dataManager import *
from flask import Flask, render_template, request

app = Flask(__name__)

data = ""
compteur = 0
score = 0
reponses = []

@app.route('/')
def home():
    restart()
    return render_template('index.html')

@app.route('/play', methods=['GET', 'POST'])
def play():

    global data
    global compteur
    global score
    global reponses

    if request.method == 'GET':
        data = pickNewData()
        compteur += 1

    if request.method == 'POST':
        user_answer = request.form.get('answer')

        if user_answer == '1':
            return render_template('endPlay.html', score=score, image_path=f"images/nul.jpg", message="Entrez un pays")

        #traite le cas d'une mauvaise orthographe
        if not isCountry(user_answer):
            return render_template('play.html', score=score, previous_guesses=reponses, dish_name=data['Nom'], image_path=f"images/plats/{data['Photo']}", message="Wrong spelling")

        # traite le cas d'une reponse déja soumise
        if alreadyAnswered(user_answer, reponses):
            return render_template('play.html', score=score, previous_guesses=reponses, dish_name=data['Nom'], image_path=f"images/plats/{data['Photo']}", message="Already answered")

        percentage = proximity_percentage(user_answer, data['Origine(pays)'])
        reponses.append((percentage, user_answer))
        reponses.sort(key=lambda x: x[0], reverse=True)

        if verifyAnswer(user_answer, data['Origine(pays)']):
            score = score + int(100 / len(reponses))
            reponses = []
            if isEndOfData():
                appreciation_photo = ""
                appreciation = score / (100*compteur)
                if appreciation < 0.34 :
                    appreciation_photo = "nul"
                if appreciation > 0.34 and appreciation < 0.67 :
                    appreciation_photo = "bof"
                else:
                    appreciation_photo = "good"
                return render_template('endPlay.html', score=score, image_path=f"images/{appreciation_photo}", message="Entrez un pays")
            else:
                data = pickNewData()
                compteur += 1
        else:
            pass
    return render_template('play.html', score=score, previous_guesses=reponses, dish_name= data['Nom'], image_path=f"images/plats/{data['Photo']}", message="Entrez un pays")

@app.route('/rule')
def rule():
    restart()
    return render_template('rule.html')


def restart():
    global data
    global compteur
    global score
    reload()
    score = 0
    compteur = 0
    data = ""

if __name__ == '__main__':
    app.run(debug=True)