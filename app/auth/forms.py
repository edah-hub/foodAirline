from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import InputRequired,Email,EqualTo
from wtforms import ValidationError
from ..models import User


class RegistrationForm(FlaskForm):
    """
    registers new users
    """

    email = StringField('Your email address...',validators=[InputRequired(),Email()])
    username = StringField('Your username...',validators=[InputRequired()])
    password = PasswordField('Your password...', validators=[InputRequired(),EqualTo('password_confirm',message='Passwords must match')])
    password_confirm = PasswordField('Confirm your password',validators=[InputRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        """
        :param data_field: email data
        :return: validated address--checks if an account exists
        """

        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        """
        :param data_field: username data
        :return: validated user--checks if username exists
        """
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username exists')


class LoginForm(FlaskForm):
    """
    signs in existing users
    """
    email = StringField('Email...',validators=[InputRequired(), Email()])
    password = PasswordField('Password...',validators=[InputRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
