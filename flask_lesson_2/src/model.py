from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, IntegerField, SubmitField
from wtforms.validators import DataRequired, InputRequired


class AddProductForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    description = TextAreaField("Description: ", validators=[DataRequired()])
    img_name = FileField("Img_name: ", validators=[InputRequired()])
    price = IntegerField("Price: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddMarketForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    location = StringField("Location: ", validators=[DataRequired()])
    img_name = FileField("Img_name: ", validators=[InputRequired()])
    submit = SubmitField("Submit")

