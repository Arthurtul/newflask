from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    data = StringField('Date', [DataRequired()])
    autor = StringField('Author', [DataRequired()])
    book_name = StringField('Title', [DataRequired()])
    comment = TextAreaField('Your post', [DataRequired(), Length(min=10, message='Too short')])
    submit = SubmitField('Submit')
