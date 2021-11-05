from flask import render_template, redirect
from app import app, db, Config
from app.models import Result
from app.forms import QuizForm, ResetForm
import psycopg2

@app.route("/result")
def success():
    avotes = Result.query.filter_by(answer = "A").count()
    bvotes = Result.query.filter_by(answer = "B").count()
    cvotes = Result.query.filter_by(answer = "C").count()
    dvotes = Result.query.filter_by(answer = "D").count()
    return render_template("result.html",
        title = "Submission Successful",
        avotes = avotes,
        bvotes = bvotes,
        cvotes = cvotes,
        dvotes = dvotes,
        totalvotes=avotes+bvotes+cvotes+dvotes+0.001 # +0.001 to prevent division by 0 error
    )

@app.route("/", methods=['GET', 'POST'])
@app.route("/quiz", methods=['GET', 'POST'])
def quiz():
    quizform = QuizForm()
    if quizform.validate_on_submit():
        db.session.add(Result(answer=quizform.answer.data))
        db.session.commit()
        return redirect("/result")
    return render_template("quiz.html", title = "Interactive Quiz", quizform=quizform)

@app.route("/reset", methods=['GET', 'POST'])
def reset():
    resetform = ResetForm()
    if resetform.validate_on_submit() and resetform.password.data=="iloveflask":
        db.session.execute('''TRUNCATE TABLE Result''')
        db.session.commit()
        return redirect("/result")
    return render_template("reset.html", title="Results & Reset", resetform=resetform)