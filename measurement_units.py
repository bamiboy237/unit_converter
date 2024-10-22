from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange

# Using Flask's form module, I created form fields to take in the value(float), and implement a dropdown to select the desired measurement unit.

class LengthConversionForm(FlaskForm):
    value = FloatField('Enter the Length Value to convert', validators=[DataRequired(), NumberRange(min=0.0)])

    from_unit = SelectField('Unit to convert from', choices=[
        ('millimeter', 'Millimeter'),
        ('centimeter', 'Centimeter'),
        ('meter', 'Meter'),
        ('kilometer', 'Kilometer'),
        ('inch', 'Inch'),
        ('foot', 'Foot'),
        ('yard', 'Yard'),
        ('mile', 'Mile')
    ], validators=[DataRequired()])

    to_unit = SelectField('Unit to convert to', choices=[
        ('millimeter', 'Millimeter'),
        ('centimeter', 'Centimeter'),
        ('meter', 'Meter'),
        ('kilometer', 'Kilometer'),
        ('inch', 'Inch'),
        ('foot', 'Foot'),
        ('yard', 'Yard'),
        ('mile', 'Mile')
    ], validators=[DataRequired()])

    Submit = SubmitField('Convert')


class TemperatureConversionForm(FlaskForm):
    value = FloatField('Enter the Temperature Value to convert', validators=[DataRequired(), NumberRange(min=0.0)])

    from_unit = SelectField('Unit to convert from', choices=[
        ('celsius', 'Celsius'),
        ('kelvin', 'Kelvin'),
        ('fahrenheit', 'Fahrenheit')
    ], validators=[DataRequired()])

    to_unit = SelectField('Unit to convert to', choices=[
       ('celsius', 'Celsius'),
        ('kelvin', 'Kelvin'),
        ('fahrenheit', 'Fahrenheit')
    ], validators=[DataRequired()])

    Submit = SubmitField('Convert')


class WeightConversionForm(FlaskForm):
    value = FloatField('Enter the weight value to convert', validators=[DataRequired(), NumberRange(min=0.0)])

    from_unit = SelectField('Unit to convert from', choices=[
        ('milligram', 'Milligram(s)'),
        ('gram', 'Gram(s)'),
        ('kilogram', 'Kilogram(s)'),
        ('ounce', 'Ounce(s)'),
        ('pound', 'Pound(s)'),
    ], validators=[DataRequired()])

    to_unit = SelectField('Unit to convert to', choices=[
       ('milligram', 'Milligram(s)'),
        ('gram', 'Gram'),
        ('kilogram', 'Kilogram(s)'),
        ('ounce', 'Ounce(s)'),
        ('pound', 'Pound(s)'),
    ], validators=[DataRequired()])

    Submit = SubmitField('Convert')