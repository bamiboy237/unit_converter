from app import app
from flask import render_template, redirect, url_for, flash
from measurement_units import LengthConversionForm, WeightConversionForm, TemperatureConversionForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

# Define routes and view functions for the unit conversion classes and templates
# Functions also contain convert_measurement functions which do the actual conversion

# Route and view function for length
@app.route('/length', methods=['GET', 'POST'])
def length():
    form = LengthConversionForm()
    if form.validate_on_submit():
        # Process selected options
        value = form.value.data
        from_unit = form.from_unit.data
        to_unit = form.to_unit.data

        # Computate Conversion
        def convert_length(value, from_unit, to_unit):
            conversion_factors = {
                'millimeter': 0.001,
                'centimeter': 0.01,
                'meter': 1,
                'kilometer': 1000,
                'inch': 0.0254,
                'foot': 0.3048,
                'yard': 0.9144,
                'mile': 1609.34
            }
            # Convert to meters first
            meters = value * conversion_factors[from_unit]
            # Then convert to the desired unit
            return meters / conversion_factors[to_unit]

        try:
            converted_value = convert_length(value, from_unit, to_unit)
            flash(f'{value} {from_unit} is {converted_value:.2f} {to_unit}', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
        
        return redirect(url_for('length'))  

    return render_template('length.html', form=form)  

# Route and view function for weight

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        'milligram': 0.000001,
        'gram': 0.001,
        'kilogram': 1,
        'ounce': 0.0283495,
        'pound': 0.453592
    }
    # Convert to kilograms first
    kilograms = value * conversion_factors[from_unit]
    # Then convert to the desired unit
    return kilograms / conversion_factors[to_unit]

@app.route('/weight', methods=['GET', 'POST'])
def weight():
    form = WeightConversionForm()
    if form.validate_on_submit():
        # Process selected options
        value = form.value.data
        from_unit = form.from_unit.data
        to_unit = form.to_unit.data

        try:
            # Compute Conversion
            converted_value = convert_weight(value, from_unit, to_unit)
            flash(f'{value} {from_unit} is {converted_value:.2f} {to_unit}', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
                
        return redirect(url_for('weight'))  

    return render_template('weight.html', form=form)

# Route and view function for temperature

def convert_temperature(value, from_unit, to_unit):
    conversion_factors = {
        'celsius': {
            'fahrenheit': lambda c: (c * 9/5) + 32,
            'kelvin': lambda c: c + 273.15
        },
        'fahrenheit': {
            'celsius': lambda f: (f - 32) * 5/9,
            'kelvin': lambda f: (f - 32) * 5/9 + 273.15
        },
        'kelvin': {
            'celsius': lambda k: k - 273.15,
            'fahrenheit': lambda k: (k - 273.15) * 9/5 + 32
        }
    }
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        raise ValueError("Invalid temperature unit provided.")

    # Convert to the desired unit
    return conversion_factors[from_unit][to_unit](value)



@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    form = TemperatureConversionForm()
    if form.validate_on_submit():
        # Process selected options
        value = form.value.data
        from_unit = form.from_unit.data
        to_unit = form.to_unit.data

        try:
            # Compute Conversion
            converted_value = convert_temperature(value, from_unit, to_unit)
            flash(f'{value} {from_unit} is {converted_value:.2f} degree {to_unit}', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
                
        return redirect(url_for('temperature'))  

    return render_template('temperature.html', form=form)