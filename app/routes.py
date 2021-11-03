from flask import render_template, request
from app import app, db, Config
from app.models import Result
from app.forms import QuizForm, ResetForm
import psycopg2

@app.route("/", methods=['GET', 'POST'])
def index():
    IPAddress = request.environ['REMOTE_ADDR']
    answer = request.form['answer']

    quizform = QuizForm()
    if quizform.validate_on_submit():
        db.session.add(Result(IPAddress=quizform.IPAddress.data, answer=quizform.answer.data))
        db.session.commit()
    
    resetform = ResetForm()
    if resetform.validate_on_submit():
        db.session.delete_all(Result.query.filter_by())
        db.session.commit()
    
    return render_template("index.html", title = "Interactive Quiz", quizform=quizform, resetform=resetform)