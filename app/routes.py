from flask import render_template, request, redirect
from app import app, db, Config
from app.models import Result
from app.forms import QuizForm
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
    """quizform.ipAddress = request.environ['REMOTE_ADDR']"""
    if quizform.validate_on_submit():
        db.session.add(Result(answer=quizform.answer.data))
        db.session.commit()
        return redirect("/success")
    """
    resetform = ResetForm()
    if resetform.validate_on_submit():
        db.session.delete_all(Result.query.filter_by())
        db.session.commit()
    """
    return render_template("quiz.html", title = "Interactive Quiz", quizform=quizform)