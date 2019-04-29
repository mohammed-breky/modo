from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class info(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=15)])
    age = StringField('Age', validators=[DataRequired()])
    item = StringField('Item', validators=[DataRequired()])

    submit = SubmitField('add')
