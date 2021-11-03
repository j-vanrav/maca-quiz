from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError
from app.models import Result

SECRET_KEY = 'iloveflask'

class QuizForm(FlaskForm):
    ipAddress   = StringField("IP Address", validators = [DataRequired()])
    answer      = StringField("Answer", validators = [DataRequired()])
    submit      = SubmitField("Submit Answer")

    # Do not allow one IP address to submit multiple answers
    def validate_ip_address(self, ipAddress):
        if Result.query.filter_by(ipAddress = ipAddress.data).first() is not None:
            raise ValidationError("You've already submitted an answer this round")

class ResetForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    def validate_password(self, password):
        if password is not SECRET_KEY:
            raise ValidationError("Incorrect password")