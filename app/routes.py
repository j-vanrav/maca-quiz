from flask import render_template, request, redirect
from app import app, db, Config
from app.models import Result
from app.forms import QuizForm, ResetForm
import psycopg2

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title = "Home Page")

@app.route("/success")
def success():
    return render_template("success.html", title = "Submission Successful")

@app.route("/quiz", methods=['GET', 'POST'])
def quiz():
    quizform = QuizForm()
    if quizform.validate_on_submit():
        db.session.add(Result(answer=quizform.answer.data))
        db.session.commit()
        return redirect("/success")
    return render_template("quiz.html", title = "Interactive Quiz", quizform=quizform)

@app.route("/reset", methods=['GET', 'POST'])
def reset():
    resetform = ResetForm()
    if resetform.validate_on_submit():
        db.session.execute('''TRUNCATE TABLE Result''')
        db.session.commit()
        return redirect("/success")
    return render_template("reset.html", title="Results & Reset", resetform=resetform)