from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired
from app.models import Result

class QuizForm(FlaskForm):
    answer      = RadioField("Answer", choices=[('A','A'),('B','B'),('C','C'),('D','D')], validators = [DataRequired()])
    submit      = SubmitField("Submit Answer")

class ResetForm(FlaskForm):
    password    = PasswordField('Password', validators=[DataRequired()])
    submit      = SubmitField("Reset Answers")
