from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField
from wtforms.validators import DataRequired

class addItem(FlaskForm):
    name = StringField('Item Name',validators=[DataRequired()])
    category = StringField('Item Category',validators=[DataRequired()])
    price = FloatField('Item Price')
    details = TextAreaField('Details')
    submit = SubmitField("Add Item")