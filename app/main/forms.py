from tokenize import String
from flask import Flask
from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import SubmitField, TextAreaField, StringField, SelectField, PasswordField,IntegerField,FileField
from wtforms.validators import InputRequired, Email, ValidationError,DataRequired,Regexp
from ..models import User


class MealForm(FlaskForm):
    """
    creates new meal objects
    """

    meal_name = StringField('What should we call this package?')
    meal_description = TextAreaField('What does this package contain?')
    meal_cost = IntegerField('How much does it cost?')
    meal_count = StringField('How many people can share the cost?')
    submit = SubmitField('Add meal')
    
    
class OrdersForm():
    """
    creates new meal objects
    """

    user_number = IntegerField('Meal Cost')
    submit = SubmitField('Add meal')


class customerLoginForm():
    """
    """
    

class Register():
    """
    """
    
class ContactForm(FlaskForm):
    """
    """
    contact_email = StringField('Email address...',validators=[InputRequired(),Email()])
    contact_name = StringField('Your name...',validators=[InputRequired()])
    contact_message = TextAreaField('Write something here...',validators=[InputRequired()])
    submit = SubmitField('Send message')
    

class checkoutForm(FlaskForm):
    name = StringField('Who will receive this order? Enter a name...',validators=[InputRequired()])
    email = StringField("Enter recipient's email...",validators=[InputRequired(),Email()])
    phone = StringField("Enter recipient's phone number...",validators=[InputRequired()])
    address = StringField("Enter recipient's home address...",validators=[InputRequired()])
    submit = SubmitField('Checkout')
    