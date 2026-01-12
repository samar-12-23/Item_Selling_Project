from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField
from wtforms.validators import length,equal_to,email,data_required,ValidationError
from app.model import User


#Registration form of the Website
class RegisterForm(FlaskForm):

    def validate_username(self,username_to_check):
        user  = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username Already Exists ! Please try a different username")


    def validate_email_address(self,email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError("Email Address already exists!! Please try a different email address")

    username = StringField(label="User Name", validators=[length(min=2,max=30),data_required()])
    email_address=StringField(label="Email Address:", validators=[email(),data_required()])
    password1 = PasswordField(label="Enter Password:", validators=[length(min=6),data_required()])
    password2 = PasswordField(label="Confirm Your Password:", validators=[equal_to('password1'),data_required()])
    submit = SubmitField(label="Create Account")


#Login form of the Website
class LoginForm(FlaskForm):
    username = StringField(label="User Name:", validators=[data_required()])
    password = PasswordField(label="Password :", validators=[data_required()])
    submit = SubmitField(label="Login Account")


#Modal Purchase-confirmation form
class PurchaseItemForm(FlaskForm):
    submit =  SubmitField(label="Purchase Item")


#Modal Sell-item form
class SellItemForm(FlaskForm):
    submit =  SubmitField(label="Sell Item")