from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import Employee

class RegistrationForm(FlaskForm):
    name = StringField('name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    def validate_name(self, field):
        if Employee.query.filter_by(name=field.data).first():
            raise ValidationError('Employee already exists', 'danger')

    designation = StringField('designation',
                       validators=[DataRequired(), Length(min=2, max=20)])
    address = StringField('address',
                          validators=[DataRequired(), Length(min=2, max=100)])
    phone = IntegerField('phone',
                          validators=[DataRequired()])
    submit = SubmitField('Add Employee')


